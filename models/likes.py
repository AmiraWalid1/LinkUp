#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from base_model import BaseModel, Base

class Like(BaseModel, Base):
    __tablename__ = "likes"
