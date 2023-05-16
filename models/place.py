#!/usr/bin/python3
"""Defines a ``BaseModel`` subclass, ``Place`` """

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Defines Place object

    Class Attributes
    ----------------
    city_id (str):
        refers to ``City.id``
    user_id (str):
        refers to ``User.id``
    name (str)
    description (str)
    number_rooms (int)
    number_bathrooms (int)
    max_guest (int)
    price_by_night (int)
    latitude (float)
    longitude (float)
    amenity_ids (list):
        list of ``id`` attributes for ``Amenity`` instances
    """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
