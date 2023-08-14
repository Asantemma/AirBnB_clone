#!/usr/bin/python3
"""This module defines class Amenity inherited from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines class Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes class Amenity"""
        super().__init__(*args, **kwargs)
