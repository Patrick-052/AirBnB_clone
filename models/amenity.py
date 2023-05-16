#!/usr/bin/python3
"""Defines ``BaseModel`` subclass, ``Amenity`` """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines Amenity object

    ...

    Class Attributes
    ----------------
    name (str):
        name of an ``Amenity`` instance
    """

    name = ''
