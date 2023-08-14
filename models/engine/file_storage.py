#!/usr/bin/python3
"""This module contains the FileStorage Class"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """class FileStorage that serializes instances to a JSON file\
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    class_dict = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                  "Place": Place, "Review": Review,
                  "State": State, "User": User}

    def all(self):
        """returns the saved objects"""
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(type(self).__file_path, "w") as f:
            new_objects = {}
            for key in type(self).__objects.keys():
                new_objects[key] = type(self).__objects[key].to_dict()
            json.dump(new_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(type(self).__file_path, "r") as f:
                json_objects = json.load(f)
            for key in json_objects.keys():
                class_name = json_objects[key]["__class__"]
                obj = type(self).class_dict[class_name](**json_objects[key])
                type(self).__objects[key] = obj
        except FileNotFoundError:
            pass
