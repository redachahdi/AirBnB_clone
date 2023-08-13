#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Represents an abstracted storage engine.

    Attributes:
        _file_path (str): The name of the file to save objects into.
        _objects (dict): A dictionary of instantiated objects.
    """
    _file_path = "file.json"
    _objects = {}

    def all(self):
        """Returns the dictionary of objects."""
        return FileStorage._objects

    def new(self, obj):
        """Adds obj to _objects with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        FileStorage._objects[key] = obj

    def save(self):
        """Serializes _objects to the JSON file _file_path."""
        object_dict = {key: obj.to_dict() for key, obj in FileStorage._objects.items()}
        with open(FileStorage._file_path, "w") as file:
            json.dump(object_dict, file)

    def reload(self):
        """Deserializes the JSON file _file_path to _objects, if it exists."""
        try:
            with open(FileStorage._file_path) as file:
                object_dict = json.load(file)
                for key, obj_data in object_dict.items():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    obj_instance = eval(class_name)(**obj_data)
                    self.new(obj_instance)
        except FileNotFoundError:
            return

