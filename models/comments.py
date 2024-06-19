#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from base_model import BaseModel, Base

class Comment(BaseModel, Base):
    __tablename__ = "comments"
    content = Column(String(500), nullable=False)
