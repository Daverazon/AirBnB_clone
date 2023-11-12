#!/usr/bin/python3
"""This module dedines a FileStorage class"""
import json

from models.user import User
from models.base_model import BaseModel


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
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        odict = FileStorage.__objects
        odict = {key: odict[key].to_dict() for key in odict.keys()}
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(odict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists; otherwise, do nothing. If the
        file doesn't exist, no exception should be raised)"""
        odict = FileStorage.__objects
        try:
            with open(FileStorage.__file_path) as f:
                odict = json.load(f)
                for dict_rep in odict.values():
                    cls = dict_rep["__class__"]
                    obj = eval(cls)(**dict_rep)  # recreate object
                    self.new(obj)  # add object to FileStorage.__objects
        except FileNotFoundError:
            pass
