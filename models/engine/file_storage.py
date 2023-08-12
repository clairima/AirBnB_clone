#!/usr/bin/python3

"""
This module contains FileStorage class,
which acts as a storage engine for our
project.
"""

import json
from os.path import exists


class FileStorage:
    """
    This class serializes instances to
    a JSON file and deserializes JSON
    file to instances
    """

    def __init__(self, file_path=None):
        """
        Constructor for the FileStorage class objects
        """
        if file_path is not None:
            self.__file_path = file_path
        else:
            self.__file_path = './file.json'
        self.__objects = {}

    def all(self):
        """
        returns __objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        <obj class name>.id
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        obj_dic = {}
        for key, value in self.__objects.items():
            obj_dic[key] = value.to_dict()
        json_objs = json.dumps(obj_dic, default=str)
        with open(self.__file_path, 'w') as f:
            return f.write(json_objs)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t
        exist.
        """
        if not exists(self.__file_path):
            return
        with open(self.__file_path, 'r') as f:
            json_objs = f.read()
            obj_dic = json.loads(json_objs)
            from models.amenity import Amenity
            from models.base_model import BaseModel
            from models.city import City
            from models.place import Place
            from models.review import Review
            from models.state import State
            from models.user import User
            for key, value in obj_dic.items():
                class_name = value['__class__']
                if class_name in locals():
                    model_class = locals()[class_name]
                    self.__objects[key] = model_class(**value)
