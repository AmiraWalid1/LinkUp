#!/usr/bin/python3
"""
initialize the models package
"""

from .engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
