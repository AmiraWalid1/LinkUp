#!/usr/bin/python3
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from base_model import BaseModel, Base

class Like(BaseModel, Base):
    __tablename__ = "likes"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    post_id = Column(String(60), ForeignKey('posts.id'), nullable=False)

    user = relationship("User", back_populates='likes')
    post = relationship("Post", back_populates='likes')
