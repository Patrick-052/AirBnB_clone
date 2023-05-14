#!/usr/bin/python3
"""Defines ``BaseModel`` subclass, ``City`` """

from models.base_model import BaseModel


class City(BaseModel):
    """Define City object"""

    state_id = ''
    name = ''
