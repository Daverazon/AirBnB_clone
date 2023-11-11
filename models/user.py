#!/usr/bin/python3
"""This module defines a User class that inherits from BaseModel class"""
from models.base_model import BaseModel
from . import storage


class User(BaseModel):
    """A User class"""
    def __init__(self, email='', password='', first_name='', last_name=''):
        """Initialise a new user"""
        super().__init__()
        storage.new(self)