#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the class City"""
        super().__init__(*args, **kwargs)
