#!/usr/bin/python3
"""This module dedines a FileStorage class"""


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON
    file to instances
    """
    __file_path = None
    # path to JSON file
    __objects = {}
    # will store all objects by <class_name>.id
    
    def __init__(self):
        """Initialise a FileStorage object"""
    
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists; otherwise, do nothing. If the
        file doesn't exist, no exception should be raised)"""
