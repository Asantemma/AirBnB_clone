#!/usr/bin/python3
"""This module defines a User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines the User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of class User"""
        super().__init__(*args, **kwargs)
