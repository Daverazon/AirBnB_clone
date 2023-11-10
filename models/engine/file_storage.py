#!/usr/bin/python3
"""This module dedines a FileStorage class"""
import json


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON
    file to instances
    """
    __file_path = "file.json"
    # path to JSON file
    __objects = {}
    # will store all objects by <class_name>.id

    def __init__(self):
        """Initialise a FileStorage object"""

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] =\
            obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists; otherwise, do nothing. If the
        file doesn't exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
