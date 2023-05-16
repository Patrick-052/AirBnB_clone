#!/usr/bin/python3
"""Defines ``BaseModel`` subclass, ``Review`` """

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines Review object

    ...

    Class Attributes
    ----------------
    place_id (str):
        refers to ``Place.id``
    user_id (str):
        refers to ``User.id``
    text (str)
    """

    place_id = ''
    user_id = ''
    text = ''
