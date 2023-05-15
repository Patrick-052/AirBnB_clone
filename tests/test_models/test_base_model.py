#!/usr/bin/python3
"""BaseModel Tests class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """TestCases for BaseModel attributes and Methods"""

    def setUp(self):
        """method holding instances to be used by
        all other methods"""
        self.bm = BaseModel()
        self.bm_kw = BaseModel(**my_dict)

    def test_init(self):
        """TestCase for the class attributes"""
        self.assertIsInstance(self.bm_kw.id, str)
        self.assertIsInstance(self.bm_kw.created_at, datetime)
        self.assertIsInstance(self.bm_kw.updated_at, datetime)
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_str(self):
        """TestCase for string represenation"""
        string = f'[BaseModel] ({self.bm.id}) {self.bm.__dict__}'
        self.assertEqual(str(self.bm), string)
        string_kw = f'[BaseModel] ({self.bm_kw.id}) {self.bm_kw.__dict__}'
        self.assertEqual(str(self.bm_kw), string_kw)

    def test_save(self):
        """TestCase for saving the changes"""
        updated_at_before = self.bm.updated_at
        self.bm.save()
        updated_at_after = self.bm.updated_at
        self.assertLess(updated_at_before, updated_at_after)
        updated_at_before_kw = self.bm_kw.updated_at
        self.bm_kw.save()
        updated_at_after_kw = self.bm_kw.updated_at
        self.assertLess(updated_at_before_kw, updated_at_after_kw)

    def test_dict(self):
        """TestCase for saving objects to a dictionary"""
        bm_dict = self.bm.to_dict()
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)


my_dict = {'my_number': 89, 'name': 'My First Model',
           '__class__': 'BaseModel', 'updated_at':
           '2017-09-28T21:05:54.119572', 'id':
           'b6a6e15c-c67d-4312-9a75-9d084935e579',
           'created_at': '2017-09-28T21:05:54.119427'}


if __name__ == '__main__':
    unittest.main()
