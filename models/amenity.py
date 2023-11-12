#!/usr/bin/python3
"""This module defines a Amenity class that inherits from BaseModel class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity of the user"""
    name = ""  # string
