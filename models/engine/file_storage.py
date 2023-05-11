#!/usr/bin/python3
"""Defines class ``FileStorage`` """

import json
from models.base_model import BaseModel


class FileStorage(BaseModel):
    """Serialize instances to a JSON file and deserialize JSON file to instances """

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """Return ``FileStorage.__objects`` """
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id """
        obj_dict = obj.to_dict()
        obj_class_name = obj_dict['__class__']
        key = obj_class_name + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize ``__objects`` to the JSON file (path: ``__file_path``) """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserialize JSON file to ``__objects`` if file exists """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
