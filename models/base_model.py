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
                if hasattr(self, key) and key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Print a description of the class instance """
        return f'[BaseModel] ({self.id}) {self.__dict__}'

    def save(self):
        """Update ``updated_at`` with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary description of the instance """
        my_dict = self.__dict__
        my_dict['__class__'] = 'BaseModel'
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
