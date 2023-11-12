#!/usr/bin/python3
"""This module defines a State class that inherits from BaseModel class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State where the user is located"""
    name = ""  # string
