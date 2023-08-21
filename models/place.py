#!/usr/bin/python3
"""that Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Describes a lodging property.
Attributes:
    city_id (str): The ID of the city where the property is located.
    user_id (str): The ID of the user who owns the property.
    name (str): The name of the property.
    description (str): A brief description of the property.
    number_rooms (int): The total number of rooms available.
    number_bathrooms (int): The total number of bathrooms available.
    max_guest (int): The maximum occupancy or number of guests allowed.
    price_by_night (int): The cost per night to stay at the property.
    latitude (float): The latitude coordinate of the property's location.
    longitude (float): The longitude coordinate of the property's location.
    amenity_ids (list): A list of IDs for associated amenities.
    """

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
