#!/usr/bin/python3
"""This module dedines a FileStorage class"""


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON
    file to instances
    """
    def __init__(self):
        """Initialise a FileStorage object"""
        self.__file_path
        # path to JSON file
        self.__objects = {}
        # will store all objects by <class_name>.id
