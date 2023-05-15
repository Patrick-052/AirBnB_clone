#!/usr/bin/python3
"""Defines class ``FileStorage`` """

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Serialize instances to a JSON file and
    deserialize JSON file to instances """

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """Return ``self.__objects`` """
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize ``__objects`` to the JSON file (path: ``__file_path``) """
        src = dict()
        for key, value in self.all().items():
            src[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(src, f, indent=4)

    def reload(self):
        """Deserialize JSON file to ``__objects`` if file exists """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
            for value in obj_dict.values():
                cls_name = value["__class__"]
                self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            return
