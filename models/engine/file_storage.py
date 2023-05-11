#!/usr/bin/python3
"""Defines class ``FileStorage`` """

import json
from models.base_model import BaseModel


class FileStorage:
    """Serialize instances to a JSON file and deserialize JSON file to instances """

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """Return ``FileStorage.__objects`` """
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id """
        obj_dict = obj.to_dict()
        obj_class_name = obj_dict['__class__']
        key = obj_class_name + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize ``__objects`` to the JSON file (path: ``__file_path``) """
        pre_json_dict = {}
        for key, value in FileStorage.__objects.items():
            pre_json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(pre_json_dict, f)

    def reload(self):
        """Deserialize JSON file to ``__objects`` if file exists """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                post_json_dict = json.load(f)

            for key in post_json_dict:
                class_name, class_id = key.split('.')
                new_obj = eval(class_name)
                FileStorage.__objects[key] = new_obj(**post_json_dict[key])

        except FileNotFoundError:
            pass
