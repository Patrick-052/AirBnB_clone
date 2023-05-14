#!/usr/bin/python3
"""City Test class"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """TestCases for City attributes and Methods"""

    def setUp(self):
        """method holding instances to be used by
        all other methods"""
        self.ct = City()

    def test_city_attr(self):
        """TestCase for presence of attribute"""
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))

    def test_city_set_attr(self):
        """TestCase for confirming equality of atttribute to
        its value"""
        self.ct.name = 'Manchester'
        self.assertEqual(self.ct.name, 'Manchester')

    def test_city_attr_type(self):
        """TestCase for checking the identity of attribute"""
        self.assertIsInstance(self.ct.name, str)

    def test_city_Baseclass(self):
        """TestCase to determine whether BaseModel is
        the class's parent class"""
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == '__main__':
    unittest.main()
