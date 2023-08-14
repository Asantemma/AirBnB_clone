#!/usr/bin/python3
"""unittests for user.py model"""

from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import unittest
import os
from models import storage
import uuid
import time


class TestUser_instantiation(unittest.TestCase):
    """User.py test case"""

    @classmethod
    def setUpClass(cls):
        """Setup unittest"""
        cls.user = User()
        cls.user.email = "me@example.com"
        cls.user.password = "175423"
        cls.user.first_name = "Emmanuel"
        cls.user.last_name = "Asante"

    def test_no_args_instantiated(self):
        self.assertEqual(User, type(User()))

    def test_instantiation(self):
        """Test instantiation of User class."""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), storage.all().values())

    def test_created_at_if_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_for_attributes_present(self):
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_if_attributes_are_strings(self):
        self.assertIs(type(self.user.email), str)
        self.assertIs(type(self.user.password), str)
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.last_name), str)

    def test_email_attribute(self):
        """Test that User has email, and it's empty"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_first_name_attribute(self):
        """Test that User has first_name, and it's empty"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name_attribute(self):
        """Test that User has last_name"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_if_to_dict_creates_dict(self):
        """test to_dict method"""
        u = User()
        dicn = u.to_dict()
        self.assertEqual(type(dicn), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in dicn)
            self.assertTrue("__class__" in dicn)

    def test_password_attribute(self):
        """Test that User has password, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_if_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_save(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.user))


if __name__ == "__main__":
    unittest.main()
