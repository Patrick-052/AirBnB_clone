#!/usr/bin/python3
"""User Tests class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """TestCases for User attributes and Methods"""

    def setUp(self):
        """method holding instances to be used by
        all other methods"""
        self.us = User()

    def test_user_attr(self):
        """TestCase for presence of attribute"""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_user_set_attr(self):
        """TestCase for confirming equality of atttribute to
        its value"""
        self.us.email = 'heisenberg@gmail.com'
        self.us.password = 'heisenberg01345'
        self.us.first_name = 'heisenberg'
        self.us.last_name = 'werner'
        self.assertEqual(self.us.email, 'heisenberg@gmail.com')
        self.assertEqual(self.us.password, 'heisenberg01345')
        self.assertEqual(self.us.first_name, 'heisenberg')
        self.assertEqual(self.us.last_name, 'werner')

    def test_user_attr_type(self):
        """TestCase for checking the identity of attribute"""
        self.assertIsInstance(self.us.email, str)
        self.assertIsInstance(self.us.password, str)
        self.assertIsInstance(self.us.first_name, str)
        self.assertIsInstance(self.us.last_name, str)

    def test_user_baseclass(self):
        """TestCase to determine whether BaseModel is
        the class's parent class"""
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main()
