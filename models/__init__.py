#!/usr/bin/python3
"""This pacakge contains the classes for the Airbnb project"""
from models.engine.file_storage import FileStorage  # use relative import


storage = FileStorage()
# create a unique FileStorage instance for my application
storage.reload()
