#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    __tablename__ = "users"
    name = Column(String(60), nullable=False)
    password = Column(String(30), nullable=False, unique=True)
    email = Column(String(30), nullable=False, unique=True)
    bio = Column(String(100), nullable=True)

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    likes = relationship("Like", back_populates="user")
