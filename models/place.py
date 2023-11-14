#!/usr/bin/python3
"""This module defines Place class that inherits from BaseModel class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Places users can stay in"""
    city_id = ""  # it will be the City.id
    user_id = ""  # it will be the User.id
    name = ""  # string
    description = ""  # string
    number_rooms = 0  # integer
    number_bathrooms = 0  # integer
    max_guest = 0  # integer
    price_by_night = 0  # integer
    latitude = 0.0  # float
    longitude = 0.0  # float
    amenities = []  # list of strings, will be the list of Amenity.id later
