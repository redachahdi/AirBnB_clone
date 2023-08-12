#!/usr/bin/python3
# that Defines the class of reviews
from models.base_model import BaseModel


class Review(BaseModel):
    #place_id ,user_id and the text are (str)
    place_id = ""
    user_id = ""
    text = ""
