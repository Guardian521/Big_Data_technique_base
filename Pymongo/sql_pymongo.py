import pymongo
import pandas as pd
#连接的用户如果是在特定数据库，而非admin数据库，需要指定认证的源数据库
uri = "mongodb://BGC_stu:Bigdatacourse123$@202.117.45.244:27017/?authSource=bdg_course"
client = pymongo.MongoClient(uri)
db = client.bdg_course
# 指定集合
col1 = db.Homework1_2216113486_谷帅_celebrity
# 读取 CSV 文件到 DataFrame
csv_file_path = '/Users/gushuai/Desktop/爬虫/大数据基础/quotetutorial/sorted_authors.csv'  # 替换为你的 CSV 文件路径
df = pd.read_csv(csv_file_path)
# 将 DataFrame 转为字典列表
data = df.to_dict(orient='records')

# 插入数据到 MongoDB 集合
col1.insert_many(data)

# 关闭连接
client.close()
