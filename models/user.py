#!/usr/bin/python3
"""difined the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """the user represent the different attribute:
    # the email (str),password (int) fisrt and last name (str)"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
