from sqlalchemy import Table,Column,Integer,ForeignKey,String,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://shop:123@127.0.0.1:3306/shop", max_overflow=5)
Base = declarative_base()
class Host(Base):
    __tablename__ = 'hosts'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(Integer,unique=True,nullable=False)
    port = Column(Integer,default=22)
    group_id = Column(Integer,ForeignKey('group.id'))
    group = relationship('Group')
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True,nullable=False)



#if __name__ == '__main__':

