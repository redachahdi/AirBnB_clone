#!/usr/bin/python3
"""base class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''
    Class BaseModel that serves as a custom base for all the classes in
    the AirBnb console project.

    Attributes:
        id (str): Handles unique user identity.
        created_at: Assigns current datetime.
        updated_at: Updates current datetime.

    Methods:
        __str__: Prints the class name, id, and creates a dictionary
                 representation of the instance's attributes.
                 [<class name>] (<self.id>) <self.__dict__>
        save(self): Updates instance attributes with the current datetime.
        to_dict(self): Returns the dictionary representation of the instance.
    '''

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)
        date_t = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, date_t))
                elif key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
