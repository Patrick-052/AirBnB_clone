#!/usr/bin/python3
"""Review Tests class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """TestCases for Review attributes and Methods"""

    def setUp(self):
        """method holding instances to be used by
        all other methods"""
        self.rw = Review()

    def test_review_attr(self):
        """TestCase for presence of attribute"""
        self.assertTrue(hasattr(Review, 'text'))
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))

    def test_review_set_attr(self):
        """TestCase for confirming equality of atttribute to
        its value"""
        self.rw.text = 'Five stars'
        self.assertEqual(self.rw.text, 'Five stars')

    def test_review_attr_type(self):
        """TestCase for checking the identity of attribute"""
        self.assertIsInstance(self.rw.text, str)

    def test_review_Baseclass(self):
        """TestCase to determine whether BaseModel is
        the class's parent class"""
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == '__main__':
    unittest.main()
