#!/usr/bin/python3
"""Defines class ``BaseModel`` """

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class """

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
        """Print a description of the class instance """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update ``updated_at`` with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary description of the instance """
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in ('created_at', 'updated_at'):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
