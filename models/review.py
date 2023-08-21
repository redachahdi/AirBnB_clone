#!/usr/bin/python3
"""that Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """Defines a review entity.
Attributes:
place_id (str): The ID of the associated place.
user_id (str): The ID of the user who wrote the review.
text (str): The content of the review.
=======
    """Represents a review.
    Attributes:
        place_id  (str): The Place id.
        user_id  (str): The User id.
        text  (str): The text of the review.
>>>>>>> 1405196ed27a8535c85859a03e4842c0e9ef4566
    """

    place_id = ""
    user_id = ""
    text = ""
