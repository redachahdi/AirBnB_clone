#!/usr/bin/python3
"""that Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review entity.
Attributes:
place_id (str): The ID of the associated place.
user_id (str): The ID of the user who wrote the review.
text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
