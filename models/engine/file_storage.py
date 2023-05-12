#!/usr/bin/python3
"""Defines class ``FileStorage`` """

import json
from models.base_model import BaseModel


class FileStorage:
    """Serialize instances to a JSON file and deserialize JSON file to instances """

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
        src = self.__objects.copy()
        for key in src:
            src[key] = src[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(src, f)

    def reload(self):
        """Deserialize JSON file to ``__objects`` if file exists """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                dest = json.load(f)
            for key in dest:
                self.__objects[key] = eval(key.split('.')[0])(dest[key])
        except FileNotFoundError:
            pass
