#!/usr/bin/python3
"""This module defines a BaseModel class"""
import uuid
from datetime import datetime

from . import storage  # use relative import


class BaseModel:
    """This class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialise a BaseModel object
        """
        if kwargs:
            # if we have a non-empty dict_representation of an
            # object, re-create that instance
            for key in kwargs.keys():
                if key == '__class__':
                    # don't add __class__ as attribute
                    continue
                if key == 'created_at':
                    self.created_at = datetime.fromisoformat(kwargs[key])
                    # convert isoformat string object to datetime object
                    continue
                if key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(kwargs[key])
                    # convert isoformat string object to datetime object
                    continue
                setattr(self, key, kwargs[key])
                # use the keys as instance attribute names to store the values
        else:
            # if it's a new instance
            self.id = str(uuid.uuid4())
            # generate unique id for each instance
            self.created_at = datetime.now()
            # assign with the current datetime when an instance is created
            self.updated_at = self.created_at
            # assign with the current datetime when an instance is created and
            # it will be updated every time you change your object
            storage.save()

    def __str__(self):
        """Return informal representation of object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return a dictionary containing all keys/values of __dict__
        of the instance
        """
        dict_representation = self.__dict__
        # create dictionary containing all instance attributes
        dict_representation['__class__'] = self.__class__.__name__
        # add class name to dictionary
        self.created_at = datetime.isoformat(self.created_at)
        # convert to string object in isoformat
        self.updated_at = datetime.isoformat(self.updated_at)
        # convert to string object in isoformat
        return dict_representation
