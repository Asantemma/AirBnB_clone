#!/usr/bin/env python3
"""Unittest for  Amenity.py Class."""

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest
import os
import uuid
import datetime
import time
from models.engine.file_storage import FileStorage
from models import storage
import json


class TestAmenity(unittest.TestCase):
    """Amenity model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.amenity = Amenity()
        cls.amenity.name = "waterbill"

    @classmethod
    def tearDownClass(cls):
        """remove class"""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes_present(self):
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    a = Amenity()

    def test_types(self):
        """tests if the type of attribute"""
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.amenity))

    def test_has_user_details(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.a, Amenity)

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)


if __name__ == "__main__":
    unittest.main()
