#!/usr/bin/python3
"""This module serializes instances to a JSON file
    and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """"serializes instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """"Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """"Serializes __objects to the JSON file"""
        data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """"Deserializes the JSON file into __objects dictionary."""
        try:
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
                for obj in data.values():
                    class_name = obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass
