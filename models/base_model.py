#!/usr/bin/python3
"""
Base Module For Air BnB Console
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base Class of AirBnb Console
    """

    def __init__(self, *args, **kwargs):
        """
        Init of Object
            Attributes:
                id(string) Random Generated by 'uuid4:(method Randome)'
                Created_at(str):Auto Generated
                    by datetime module now(get current time)
                Updated_at(str):Auto Generated by datetime and
                    generated again when object modified
                    by adding it to method that change object like save
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()
        # each new instance created is added to the storage variable __objects
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for _key, _val in kwargs.items():
                if "__class__" not in _key:
                    setattr(self, _key, _val)

    def __str__(self):
        """
        print the instance
        :return:
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """
            for now just update update_at
        """
        self.updated_at = datetime.now()
        # only when we save the instance, its writen into the json file
        models.storage.save()

    def to_dict(self):
        """
            convert  self dict and other public instance
                Return: Dictionary
        """
        _r_dic = dict(self.__dict__)
        _r_dic['__class__'] = self.__class__.__name__
        _r_dic['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        _r_dic['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return _r_dic
