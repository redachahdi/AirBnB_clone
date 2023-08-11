#!/usr/bin/python3
"""to json and the oposite"""
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {}
            for k, v in FileStorage.__objects.items():
                d[k] = v.to_dict()
            json.dump(d, f)

    def reload(self):
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
        recreated_objects = {}
        for key, serialized_data in obj_dict.items():
            class_name = serialized_data["__class__"]
            class_constructor = self.classes()[class_name]
            instance = class_constructor(**serialized_data)
            recreated_objects[key] = instance
