#!/usr/bin/python3
"""Module for User class
Contains the User class for the AirBnB clone console.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

Base = declarative_base()


class User(BaseModel, Base):
    """Represents a User in the system."""

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
