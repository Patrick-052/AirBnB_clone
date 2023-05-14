#!/usr/bin/python3
"""Place Tests class"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """TestCases for Place attributes and Methods"""

    def setUp(self):
        """method holding instances to be used by
        all other methods"""
        self.pc = Place()

    def test_place_attr(self):
        """TestCase for presence of attribute"""
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_place_attr_type(self):
        """TestCase for checking the identity of attribute"""
        self.assertIsInstance(self.pc.name, str)
        self.assertIsInstance(self.pc.description, str)
        self.assertIsInstance(self.pc.number_rooms, int)
        self.assertIsInstance(self.pc.number_bathrooms, int)
        self.assertIsInstance(self.pc.max_guest, int)
        self.assertIsInstance(self.pc.price_by_night, int)
        self.assertIsInstance(self.pc.latitude, float)
        self.assertIsInstance(self.pc.longitude, float)
        self.assertIsInstance(self.pc.amenity_ids, list)

    def test_set_place_attr(self):
        """TestCase for confirming equality of atttribute to
        its value"""
        self.pc.name = 'slovenia'
        self.pc.description = 'snowy'
        self.pc.number_rooms = 5
        self.pc.number_bathrooms = 3
        self.pc.max_guest = 3
        self.pc.price_by_night = 35000
        self.pc.latitude = 14.4
        self.pc.longitude = 20.5
        self.assertEqual(self.pc.name, 'slovenia')
        self.assertEqual(self.pc.description, 'snowy')
        self.assertEqual(self.pc.number_rooms, 5)
        self.assertEqual(self.pc.number_bathrooms, 3)
        self.assertEqual(self.pc.max_guest, 3)
        self.assertEqual(self.pc.price_by_night, 35000)
        self.assertEqual(self.pc.latitude, 14.4)
        self.assertEqual(self.pc.longitude, 20.5)

    def test_place_Baseclass(self):
        """TestCase to determine whether BaseModel is
        the class's parent class"""
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == '__main__':
    unittest.main()
