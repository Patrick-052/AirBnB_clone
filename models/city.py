#!/usr/bin/python3
"""Defines ``BaseModel`` subclass, ``City`` """

from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines City object

    ...

    Class Attributes
    ----------------
    state_id (str):
        Refers to ``State.id``
    name (str)

    """

    state_id = ''
    name = ''
