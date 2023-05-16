#!/usr/bin/python3
"""Defines storage class ``FileStorage`` """

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Maintains a dictionary of class instances.

    Records new class instances into the objects dictionary

    Saves the objects dictionary into a file for retrieval
    when the application is launched

    ...

    Attributes
    ----------
    __file_path (str):
        path to storage file (JSON file)
    __objects (dict):
        stores all objects by ``<object_class_name.object_id>``
    """

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """Return ``self.__objects`` """
        return self.__objects

    def new(self, obj):
        """Set in ``__objects`` the object(``obj``) with key
        ``<obj_class_name>.id`` """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize ``__objects`` to ``__file_path`` """
        src = dict()
        for key, value in self.all().items():
            src[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(src, f, indent=4)

    def reload(self):
        """Deserialize ``__file_path`` to ``__objects`` if the storage file
        exists """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
            for value in obj_dict.values():
                cls_name = value["__class__"]
                self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            return
