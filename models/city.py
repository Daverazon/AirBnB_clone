#!/usr/bin/python3
"""This module defines a City class that inherits from BaseModel class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City where the user is located"""
    state_id = ""  # string, it will be the State.id
    name = ""  # string
