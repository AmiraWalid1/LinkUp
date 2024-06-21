#!/usr/bin/python3
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from base_model import BaseModel, Base

class Post(BaseModel, Base):
    __tablename__ = "posts"
    content = Column(String(1000), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')
    likes = relationship('Like', back_populates='post')