#!/usr/bin/python3
"""This module defines a BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """This class defines all common attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4()) #generate unique id for each instance
        self.created_at = datetime.now() #assign with the current datetime when an instance is created
        self.updated_at = self.created_at #assign with the current datetime when an instance is created and
        # it will be updated every time you change your object

    def __str__(self):
        """Return informal representation of object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()


    def to_dict(self):
        """return a dictionary containing all keys/values of __dict__ of the instance
        """
        json_representation = self.__dict__ #create dictionary containing all instance attributes
        json_representation['__class__'] = self.__class__.__name__ #add class name to dictionary
        self.created_at = datetime.isoformat(self.created_at) #convert to string object in isoformat
        self.updated_at = datetime.isoformat(self.updated_at) #convert to string object in isoformat
        return json_representation
