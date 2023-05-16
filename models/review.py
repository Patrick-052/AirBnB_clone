#!/usr/bin/python3
"""Defines ``BaseModel`` subclass, ``Review`` """

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines Review object"""

    place_id = ''
    user_id = ''
    text = ''
