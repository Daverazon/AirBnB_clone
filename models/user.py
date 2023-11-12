#!/usr/bin/python3
"""This module defines a User class that inherits from BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """A User class"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
