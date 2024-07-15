#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from flask_login import UserMixin

class User(BaseModel, Base, UserMixin):
    __tablename__ = "users"
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    username = Column(String(60), nullable=False)
    password = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    bio = Column(String(100), nullable=False)
    country = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)
    website = Column(String(255), nullable=True) 
    photo = Column(String(255), nullable=True)  # column for storing photo path or URL

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    likes = relationship("Like", back_populates="user")
