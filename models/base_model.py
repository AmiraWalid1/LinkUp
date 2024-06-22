#!/usr/bin/python3
from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.now(timezone.utc))

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(key, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs.keys():
                self.created_at = datetime.now(timezone.utc)
            if "updated_at" not in kwargs.keys():
                self.updated_at = datetime.now(timezone.utc)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def to_dict(self):
        """Convert instance into dict format"""
        my_dict = dict(self.__dict__)
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def save(self):
        '''Save obj in database'''
        self.updated_at = datetime.now(timezone.utc)
        models.storage.new(self)
        models.storage.save()

    def update(self, **kwargs):
        """Update attribute of obj"""
        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            setattr(self, key, value)
        self.updated_at = datetime.now(timezone.utc)
        models.storage.save()

    def delete(self):
        '''Delete obj from database'''
        models.storage.delete(self)
        models.storage.save()
