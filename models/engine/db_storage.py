#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.post import Post
from models.comment import Comment
from models.like import Like


class DBStorage:
    """class to manage db storage for hbnb clone"""

    __engine = None
    __session = None
    classes = [User, Post, Comment, Like]

    def __init__(self):
        user = getenv("MYSQL_USER")
        passwd = getenv("MYSQL_PWD")
        db = getenv("MYSQL_DB")
        host = getenv("MYSQL_HOST")
        env = getenv("ENV")

        # When pool_pre_ping=True is set, SQLAlchemy issues a simple "ping"(often a lightweight SQL query like SELECT 1)
        # to the database before giving the connection to the application. If the connection is no longer valid,
        # SQLAlchemy will automatically remove it from the pool and create a new one.
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        # Base.metadata.drop_all method is used to drop all the tables that are defined in the Base metadata.
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        "reload data from the database"
        Base.metadata.create_all(self.__engine)
        # Session Factory: The sessionmaker function creates a factory for sessions.
        #   The expire_on_commit=False argument ensures that objects are not expired after committing a transaction,
        #   meaning they can still be accessed without refreshing from the database.
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        # Scoped Session: scoped_session is used to manage sessions, especially useful in web applications where each request needs a separate session.
        self.__session = scoped_session(session_factory)

    def all(self, clss=None):
        '''query on the database session'''
        my_dict = {}
        if clss and clss in self.classes:
            objs = self.__session.query(clss).all()
            for obj in objs:
                key = obj.__class__.__name__+'.'+obj.id
                my_dict[key] = obj
        else:
            for clss in self.classes:
                objs = self.__session.query(clss).all()
                for obj in objs:
                    key = obj.__class__.__name__+'.'+obj.id
                    my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        '''remove the session'''
        self.__session.remove()

    def get(self, cls, id):
        '''Get obj by id'''
        if not cls or cls not in self.classes or not id:
            return None
        return self.__session.query(cls).filter_by(id=id).first()

    def count(self, cls=None):
        """Count number of obj of class or all classes."""
        if cls:
            if cls in self.classes:
                return self.__session.query(cls).count()
            else:
                return 0
        else:
            return sum(self.__session.query(cls).count()
                       for cls in self.classes)
