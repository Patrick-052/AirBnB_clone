#!/usr/bin/python3
"""Amenity Test class"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """TestCases for Amenity attributes and Methods"""

    def setUp(self):
        """method holding instances to be used by
        all other methods"""
        self.amenity = Amenity()

    def test_amenity_attr(self):
        """TestCase for presence of attribute"""
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_amenity_set_attr(self):
        """TestCase for confirming equality of atttribute to
        its value"""
        self.amenity.name = 'conference hall'
        self.assertEqual(self.amenity.name, 'conference hall')

    def test_ammenity_attr_type(self):
        """TestCase for checking the identity of attribute"""
        self.assertIsInstance(self.amenity.name, str)

    def test_amenity_Baseclass(self):
        """TestCase to determine whether BaseModel is
        the class's parent class"""
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
