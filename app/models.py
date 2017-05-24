# -*- coding: utf-8 -*-
#from app import db
from sqlalchemy import Column, create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.types import *

from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
BaseModel = declarative_base()

# ROLE_USER = 0
# ROLE_ADMIN = 1

# class User(BaseModel):
#     id = Column(Integer, primary_key = True)
#     nickname = Column(String(64), unique = True)
#     email = Column(String(120), index = True, unique = True)
#     role = Column(SmallInteger, default = ROLE_USER)
#     #posts = relationship('Post', backref = 'author', lazy = 'dynamic')
    
#     def is_authenticated(self):
#         return True

#     def is_active(self):
#         return True

#     def is_anonymous(self):
#         return False

#     def get_id(self):
#         return unicode(self.id)

#     def __repr__(self):
#         return '<User %r><role %d>' % (self.nickname,self.role)   
        
# class Post(BaseModel):
#     id = Column(Integer, primary_key = True)
#     body = Column(String(140))
#     timestamp = Column(DateTime)
#     user_id = Column(Integer, ForeignKey('user.id'))

#     def __repr__(self):
#         return '<Post %r>' % (self.body)


# # 初始化数据库连接:
# engine = create_engine('mysql+mysqlconnector://root:haoxin123@localhost:3306/test')
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)


###数据库表的设计




#####生产企业相关表
class factorycompo_table(BaseModel):
    # 表的名字:生产企业提供的部件生产信息表
    __tablename__ = 'factorycompo_table'

    # 表的结构:
    factoryCompoId=Column(Integer, primary_key = True,autoincrement=True)
    factoryId=Column(Integer, nullable=False)
    compoType=Column(String(255),nullable=False)
    compoMaxCount=Column(Integer,nullable=False)
    attributeNames=Column(String(255))
    compoInfo=Column(String(255))
    componentImages=Column(String(500))
    productLineImages=Column(String(500))
    price=Column(Float)

    #自定义输出方式
    def __repr__(self):
        return '<factorycompo_table %s>' % (self.compoType)

class comattrvalues_table(BaseModel):
    # 表的名字:工厂生产的部件定制属性的取值范围表
    __tablename__ = 'comattrvalues_table'

    # 表的结构:
    comAttrValuesId=Column(Integer, primary_key = True,autoincrement=True)
    compoType=Column(String(255), nullable=False)
    factoryId=Column(Integer,nullable=False)
    attributeName=Column(String(255),nullable=False)
    values=Column(String(255),nullable=False)

    #自定义输出方式
    def __repr__(self):
        return '<comattrvalues_table %s>' % (self.compoType)

class virtualplatfactorycapac_table(BaseModel):
    # 表的名字:虚拟工厂工厂产能（与生产企业关联）表,算是一张公共表
    __tablename__ = 'virtualplatfactorycapac_table'

    # 表的结构:
    virtualPlatFactoryId=Column(Integer, primary_key = True,autoincrement=True)
    virtualPlatformId=Column(Integer, nullable=False)
    factoryId=Column(Integer,nullable=False)
  
    #自定义输出方式
    def __repr__(self):
        return '<comattrvalues_table %d>' % (self.virtualPlatFactoryId)


class factoryinfo_table(BaseModel):
    # 表的名字:生产企业基本信息表
    __tablename__ = 'factoryinfo_table'

    # 表的结构:
    factoryId=Column(Integer, primary_key = True,autoincrement=True)
    factoryType=Column(Integer)
    factoryName=Column(String(255),nullable=False)
    factoryOrganICode=Column(String(255),unique=True)
    factoryLegalRepre=Column(String(255),nullable=False)
    factoryTelephone=Column(String(255),nullable=False)
    factoryAddress=Column(String(255))
    factoryPeopNum=Column(Integer)
    factoryFileImages=Column(String(500))


    #自定义输出方式
    def __repr__(self):
        return '<factorycompo_table %s>' % (self.factoryName)

class virtualplatneworder_table(BaseModel):
    # 表的名字:生产企业订单表
    __tablename__ = 'virtualplatneworder_table'

    # 表的结构:
    factoryOrderId=Column(Integer, primary_key = True,autoincrement=True)
    orderNumber=Column(String(255),nullable=False,unique=True)
    compoType=Column(String(255),nullable=False)
    deadline=Column(Date)
    factoryId=Column(Integer,nullable=False)
    virtualPlatId=Column(Integer,nullable=False)
    completed=Column(Float)
    responsName=Column(String(255))
    responsPhone=Column(String(255))
    productionSiteVideo=Column(String(500))
    time=Column(DateTime)
    compoCount=Column(Integer)
    status=Column(Integer)
    attributeNames=Column(String(255))
    attributeValues=Column(String(255))


    #自定义输出方式
    def __repr__(self):
        return '<factoryOrderId %s>' % (self.compoType)     

#消费者相关表 
class consumerinfo_table(BaseModel):
    # 表的名字:消费者基本信息
    __tablename__ = 'customerinfo_table'

    # 表的结构:
    consumerId=Column(Integer, primary_key = True,autoincrement=True)
    name=Column(String(255),nullable=False)
    realName=Column(String(255))
    password=Column(String(255),nullable=False)
    phoneNumber=Column(String(255),nullable=False)
    specificAddress=Column(String(255),nullable=False)
    focusProdList=Column(String(255))


    #自定义输出方式
    def __repr__(self):
        return '<customerinfo_table %s>' % (self.name)


class consumer_order_table(BaseModel):
    # 表的名字:消费者需求表
    __tablename__ = 'customer_order_table'

    # 表的结构:
    consumerOrderId=Column(Integer, primary_key = True,autoincrement=True)
    productType=Column(String(255),nullable=False)
    virtualPlatformId=Column(Integer,nullable=False)
    count=Column(Integer,nullable=False)
    address=Column(String(255),nullable=False)
    deliverDate=Column(Date,nullable=False)
    priorityAlgo=Column(Integer)
    orderTime=Column(DateTime)
    consumerId=Column(Integer)


    #自定义输出方式
    def __repr__(self):
        return '<customer_order_table %s>' % (self.productType)

#虚拟工厂相关表
class virtualPlatCapacity_table(BaseModel):
    # 表的名字:虚拟工厂方案产能表<不同产品多个方案，一个产品多个方案>
    __tablename__ = 'virtualPlatCapacity_table'

    # 表的结构:
    virtualPlatCapacityId=Column(Integer, primary_key = True,autoincrement=True)
    virtualPlatformId=Column(Integer,nullable=False)
    productType=Column(String(255),nullable=False)
    productMaxCount=Column(Integer,nullable=False)
    images=Column(String(500))
    factoryCompoIdList=Column(String(255))
    factoryCompoCountList=Column(String(255))
    price=Column(Float,nullable=False)
    expTime=Column(Integer)



    #自定义输出方式
    def __repr__(self):
        return '<virtualPlatCapacity_table %s>' % (self.productType)

class virtualplatinfo_table(BaseModel):
    # 表的名字:虚拟工厂基本信息表
    __tablename__ = 'virtualplatinfo_table'

    # 表的结构:
    virtualPlatformId=Column(Integer, primary_key = True,autoincrement=True)
    name=Column(String(255),nullable=False)
    address=Column(String(255),nullable=False)
    organizationCode=Column(String(255),nullable=False)
    legalRepresentative=Column(String(255),nullable=False)
    phoneNumber=Column(String(255),nullable=False)
    qualDocImages=Column(String(500))
    
    #自定义输出方式
    def __repr__(self):
        return '<virtualplatinfo_table %s>' % (self.name)

class virtualplatorder_table(BaseModel):
    # 表的名字:虚拟工厂产品订单
    __tablename__ = 'virtualplatorder_table'

    # 表的结构:
    virtualPlatOrderId=Column(Integer, primary_key = True,autoincrement=True)
    factoryOrderIdList=Column(String(255),nullable=False)
    status=Column(Integer)
    virtualPlatCapacityId=Column(Integer)
    consumerOrderId=Column(Integer)
    requirement=Column(String(500))

    #自定义输出方式
    def __repr__(self):
        return '<virtualplatorder_table %s>' % (self.virtualPlatOrderId)

##三种角色登录信息
class consumerlog_table(BaseModel):
    # 表的名字:消费者登陆表
    __tablename__ = 'consumerlog_table'

    # 表的结构:
    consumerLogId=Column(Integer, primary_key = True,autoincrement=True)
    consumerId=Column(Integer,nullable=False)
    name=Column(String(255),nullable=False)
    password=Column(String(255),nullable=False)

    #自定义输出方式
    def __repr__(self):
        return '<consumerlog_table %s>' % (self.name)

class virtualplatlog_table(BaseModel):
    # 表的名字:虚拟工厂登陆表
    __tablename__ = 'virtualplatlog_table'

    # 表的结构:
    virtualPlatLogId=Column(Integer, primary_key = True,autoincrement=True)
    virtualPlatformId=Column(Integer,nullable=False)
    name=Column(String(255),nullable=False)
    password=Column(String(255),nullable=False)

    #自定义输出方式
    def __repr__(self):
        return '<virtualplatlog_table %s>' % (self.name)

class factorylog_table(BaseModel):
    # 表的名字:生产工厂登陆表
    __tablename__ = 'factorylog_table'

    # 表的结构:
    factoryLogId=Column(Integer, primary_key = True,autoincrement=True)
    factoryId=Column(Integer,nullable=False)
    name=Column(String(255),nullable=False)
    password=Column(String(255),nullable=False)

    #自定义输出方式
    def __repr__(self):
        return '<virtualplatlog_table %s>' % (self.name)

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:haoxin123@localhost:3306/trs')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all(engine)


if __name__ == '__main__':
    init_db()
    #drop_db()
    #BaseModel.metadata.tables['user'].create(Engine, checkfirst=True)
    #BaseModel.metadata.tables['user'].drop(Engine, checkfirst=False)
    pass