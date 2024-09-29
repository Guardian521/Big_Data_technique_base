from sqlalchemy import create_engine,Column, Integer, String,DateTime,INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from datetime import datetime
# 创建数据库引擎
engine = create_engine("mysql+pymysql://BGC_stu:Bigdatacourse123@202.117.45.244:33306/bgd_course?charset=utf8", echo=True)


# 创建表
Base = declarative_base()

class basicinfo(Base):
    __tablename__ = 'Homework2_2216113486_谷帅_basic_info'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, nullable=False, comment='user')
    sku = Column(String(50), nullable=False, comment='sku')
    column_3 = Column(String(50), nullable=False, comment='column_3')
    sunglasses = Column(String(50), nullable=False, comment='sunglasses')
    category = Column(String(100), nullable=False, comment='category')
    image_path = Column(String(255), nullable=False, comment='image_Path')
    number = Column(String(100), default=None,nullable=False, comment='number')
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, comment='time')

    def __repr__(self):
        return f"basicinfo:(user={self.user}, sku={self.sku}, column_3={self.column_3}, sunglasses={self.sunglasses}, category={self.category}, image_path={self.image_path}, number={self.number}, timestamp={self.timestamp})"

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


df = pd.read_csv('/Users/gushuai/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/897f26951a3817cd2e800991b8bc7376/Message/MessageTemp/6ca7cdaf52800c796e0ee86e23411084/File/basic_info.csv', delimiter=',',header=None)# 将数据插入数据库表
print(df)
# 修改为正确的列名
# 修改为正确的列名
for i in range(df.shape[0]):
    row=df.iloc[i,:]
    basic_info = basicinfo(
        user=row[0],
        sku=row[1],
        column_3=row[2],
        sunglasses=row[3],
        category=row[4],
        image_path=row[5],
        number=row[6],
        timestamp=datetime.strptime(row[7], '%Y/%m/%d %H:%M:%S')
    )
    session.add(basic_info)

session.commit()
session.close()

print("Data inserted into the database.")


re=session.query(basicinfo).all()
print(re)
'''
course_obj = Course(course_name='Python', teacher_name='Teacher liu', class_times=30)
session.add(course_obj)
course_obj1 = Course(course_name='Big data', teacher_name='Teacher zhang', class_times=30)
course_obj2 = Course(course_name='Python', teacher_name='Teacher wang', class_times=30)
session.add_all( [course_obj1, course_obj2] )
session.commit()
session.close()
'''