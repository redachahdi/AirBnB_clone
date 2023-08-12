#!/usr/bin/python3
""" that define the class """
from models.base_model import BaseModel


class Place(BaseModel):
    """city_id and user_id and  The name of the place.
    #descriptionis  (str).
    #number_rooms and
    #number_bathrooms and max_guest and price_by_night are (int)
    #latitude and longitude are (float)
    #amenity_ids (list)"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
