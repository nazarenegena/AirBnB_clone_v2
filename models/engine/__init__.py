#!/usr/bin/python3
"""
This module defines the storage engine for the application
"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
