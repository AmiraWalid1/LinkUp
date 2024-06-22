#!/usr/bin/python3
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base


class Comment(BaseModel, Base):
    __tablename__ = "comments"
    content = Column(String(500), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    post_id = Column(String(60), ForeignKey('posts.id'), nullable=False)

    user = relationship("User", back_populates='comments')
    post = relationship("Post", back_populates='comments')
