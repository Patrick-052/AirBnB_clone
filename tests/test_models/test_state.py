#!/usr/bin/python3
"""State Tests class"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """TestCases for State attributes and Methods"""

    def setUp(self):
        """method holding instances to be used by
        all other methods"""
        self.st = State()

    def test_state_attr(self):
        """TestCase for presence of attribute"""
        self.assertTrue(hasattr(State, 'name'))

    def test_state_set_attr(self):
        """TestCase for confirming equality of atttribute to
        its value"""
        self.st.name = 'Madrid'
        self.assertEqual(self.st.name, 'Madrid')

    def test_state_attr_type(self):
        """TestCase for checking the identity of attribute"""
        self.assertIsInstance(self.st.name, str)

    def test_state_Baseclass(self):
        """TestCase to determine whether BaseModel is
        the class's parent class"""
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main()
