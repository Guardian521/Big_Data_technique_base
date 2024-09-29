from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum  , corr
from pyspark.sql.types import IntegerType, DoubleType
import matplotlib.pyplot as plt
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import RegressionEvaluator

spark = SparkSession.builder.appName("CorrelationCalculation").getOrCreate()

# 读取
df1 = spark.read.csv("/Users/gushuai/Downloads/data.csv", header=True, inferSchema=True)
df2 = spark.read.csv("/Users/gushuai/Downloads/data (9).csv", header=True, inferSchema=True)

# 处理 df2：去重 tokens_address 列，删除缺失值所在的整行
df2 = df2.dropDuplicates(["tokens_address"])
df2 = df2.dropna(subset=["tokens_decimals"])
df2 = df2.na.drop()
df1 = df1.withColumn("token_transfers_value", col("token_transfers_value").cast(IntegerType()))
result_df = df1.groupBy("token_transfers_token_address").agg(sum("token_transfers_value").alias("total_value"))
df2 = df2.withColumn("tokens_decimals", col("tokens_decimals").cast(DoubleType()))
merged_df = result_df.join(df2, result_df["token_transfers_token_address"] == df2["tokens_address"], "inner")

# 计算相关性
correlation_df = merged_df.select(corr("tokens_decimals", "total_value").alias("correlation"))

correlation_df.show()

#绘制代币最小单位和代币交易总量折线图
pandas_df = merged_df.orderBy("tokens_decimals").select("tokens_decimals", "total_value").toPandas()
pandas_df = pandas_df[pandas_df["tokens_decimals"] <= 10]
plt.plot(pandas_df["tokens_decimals"], pandas_df["total_value"])
plt.xlabel("tokens_decimals")
plt.ylabel("total_value")
plt.title("Relationship between tokens_decimals and total_value")
plt.show()


assembler = VectorAssembler(inputCols=["tokens_decimals"], outputCol="features")
feature_df = assembler.transform(merged_df).select("features", "total_value")

#建模与预测
lr = LinearRegression(featuresCol="features", labelCol="total_value", maxIter=10, regParam=0.01)
pipeline = Pipeline(stages=[assembler, lr])
model = pipeline.fit(merged_df)
predictions = model.transform(merged_df)
predictions.select("tokens_decimals", "total_value", "prediction").show()

#结果检验
evaluator = RegressionEvaluator(labelCol="total_value", predictionCol="prediction", metricName="rmse")
r2 = evaluator.evaluate(predictions, {evaluator.metricName: "r2"})
print(f"R-squared (R2): {r2}")