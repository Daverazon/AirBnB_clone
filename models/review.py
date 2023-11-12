#!/usr/bin/python3
"""This module defines a Review class that inherits from BaseModel class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """User reviews"""
    place_id = ""  # string, it will be the Place.id
    user_id = ""  # string, it will be the User.id
    text = ""  # string
