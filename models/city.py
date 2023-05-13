#!/usr/bin/python3
"""Defines ``BaseModel`` subclass, ``City`` """

from models.base_model import BaseModel


class City(BaseModel):
    """City """

    state_id = ''
    name = ''
