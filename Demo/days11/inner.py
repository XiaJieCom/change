from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+pymysql://shop:123@localhost:3306/shop',echo=True)

SessionCls = sessionmaker(bind=engine)
session = SessionCls()

