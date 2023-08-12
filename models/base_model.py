#!/usr/bin/python3
"""base class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''
    Class BaseModel that a Custom base for all the classes in
    the AirBnb console project:

    Arttributes:
            id(str): handles unique user identity
            created_at: assigns current datetime
            upddated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
                 representations of the input values
                 [<class name>] (<self.id>) <self.__dict__>
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj
    '''
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)
        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct