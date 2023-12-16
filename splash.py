from sqlalchemy import create_engine,String,Column,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str(uuid.uuid4())
Base = declarative_base()

class Member(Base):
    __tablename__='members'
    memberId = Column('memberId',String,primary_key=True,default=generate_uuid)
    memberName = Column('memberName',String)
    memberEmail = Column('memberEmail',String)
    memberAge = Column('memberAge',Integer)
    
    def __init__(self,memberName,memberEmail,memberAge):
        self.memberName = memberName
        self.memberEmail = memberEmail
        self.memberAge = memberAge

db = 'sqlite:///newDB.db'
engine = create_engine(db)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()    

def add_member(memberName,memberAge,memberEmail,):
    exists = session.query(Member).filter_by(memberEmail=memberEmail).first()
    if exists:
        print('Email already exists') 
    else:
        new_member=Member(memberName=memberName,memberAge=memberAge,memberEmail=memberEmail)
        session.add(new_member)
        session.commit()    

memberName = 'Am'
memberEmail='am@gmail.com'
memberAge = 16
add_member(memberName,memberAge,memberEmail)
