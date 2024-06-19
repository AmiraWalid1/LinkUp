#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from base_model import BaseModel, Base

class Post(BaseModel, Base):
    __tablename__ = "posts"
    content = Column(String(1000), nullable=False)
