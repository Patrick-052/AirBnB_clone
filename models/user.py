#!usr/bin/python3
"""Defines a ``BaseModel`` subclass, ``User`` """

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines user information

    ...

    Class Attributes
    ----------------
    email (str)
    password (str)
    first_name (str)
    last_name (str)
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
