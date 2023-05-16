#!/usr/bin/python3
"""Defines a base class ``BaseModel`` """

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Defines common attributes and methods for other classes in the application

    ...

    Class Attributes
    ----------------
    id (str):
        unique identifier for a class instance
    created_at (datetime):
        refers to the time an instance was created
    updated_at (datetime):
        refers to the time an instance was updated

    Additional attributes may be set based on the ``kwargs`` parameter of the
    constructor method
    """

    def __init__(self, *args, **kwargs):
        """Constructor method """
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Print a description of a ``BaseModel`` instance """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Save changes made to a ``BaseModel`` instance """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary description of a ``BaseModel`` instance """
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in ('created_at', 'updated_at'):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
