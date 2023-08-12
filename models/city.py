#!/usr/bin/python3
"""that Defines the class of the city"""
from models.base_model import BaseModel


class City(BaseModel):
    """state_id (str): the id of the state.
    name (str): the city name"""
    state_id = ""
    name = ""
