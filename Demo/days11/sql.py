from sqlalchemy import  create_engine,Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

'''
metadata = MetaData()

user = Table('user',metadata,
             Column('id',Integer,primary_key=True),
             Column('name',String(20)),
             )
color = Table('color',metadata,
             Column('id',Integer,primary_key=True),
             Column('name',String(20)),
             )
'''

Base = declarative_base()
engine = create_engine('mysql+pymysql://shop:123@localhost:3306/shop',echo=True)

metadata = MetaData()

Host2Group = Table('host_2_group',Base.metadata,
               Column('host_id',ForeignKey('hosts.id'),primary_key=True),
               Column('group_id',ForeignKey('group.id'),primary_key=True)
               )

class Host(Base):
    __tablename__ = 'hosts'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)
    groups = relationship('Group',
                          secondary=Host2Group,
                          backref='host_list'
                          )
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True,nullable=False)






Base.metadata.create_all(engine)
if __name__ == '__main__':

    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()
    #h1 = Host(hostname='localhost',ip_addr='127.0.0.1')
    #h2 = Host(hostname='ubuntu',ip_addr='192.168.2.243',port=20000)
    #h3 = Host(hostname='ubuntu2',ip_addr='192.168.2.244',port=20000)
    #session.add_all([h1,h2,h3])
    g1 = session.query(Group).first()
    h1 = session.query(Host).filter(Host.hostname == 'h1').first()
    h1.groups = groups[1:-1]
    '''
    res = session.query(Host).filter_by(hostname = 'ubuntu2').first()
    print(res)
    res.hostname = 'nginx'
    '''
    #g1 = Group(name='g1')
    #g2 = Group(name='g2')
    #g3 = Group(name='g3')
    #g4 = Group(name='g4')
    #session.add_all([g1,g2,g3,g4])
    session.commit()