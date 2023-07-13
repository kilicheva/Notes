from sqlalchemy import Column, Integer, String, Boolean
from .db import Base


class Users(Base):

    __tablename__ = 'users'

    login = Column(String, unique=True, index=True, primary_key=True)
    password = Column(String)
    email = Column(String)
    phone_number = Column(String)


class Post(Base):

    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, index=True,  unique=True)
    title = Column(String)
    content = Column(String)
    status = Column(String)
    published = Column(Boolean)


