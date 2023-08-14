#!/usr/bin/python3
"""This module defines class Review inherited from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """defines class for review object."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes class Review"""
        super().__init__(*args, **kwargs)
