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
        obj_dict = obj.to_dict()
        obj_class_name = obj_dict['__class__']
        key = obj_class_name + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize ``__objects`` to the JSON file (path: ``__file_path``) """
        src = {}
        for key, value in self.__objects.items():
            src[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(src, f)

    def reload(self):
        """Deserialize JSON file to ``__objects`` if file exists """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                dest = json.load(f)

            for key in dest:
                class_name, class_id = key.split('.')
                new_obj = eval(class_name)
                self.__objects[key] = new_obj(**dest[key])

        except FileNotFoundError:
            pass
