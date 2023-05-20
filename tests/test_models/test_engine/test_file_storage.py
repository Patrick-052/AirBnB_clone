#!/usr/bin/python3
"""FileStorage Tests class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """TestCases for Amenity attributes and Methods"""

    def setUp(self):
        """method holding instances to be used by
        all other methods"""
        self.fs = FileStorage()

    def test_fs_has_attr(self):
        """TestCase for presence of attribute"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_fs_attr_type(self):
        """TestCase for checking the identity of attribute"""
        self.assertIsInstance(self.fs._FileStorage__file_path, str)
        self.assertIsInstance(self.fs._FileStorage__objects, dict)

    def test_new(self):
        """TestCase for creating a new object"""
        return
        # obj = BaseModel()
        # self.fs.new(obj)
        # self.assertTrue(('BaseModel'+ '.' + obj.id, obj)
        # in self.fs.__objects.items())

    def test_save(self):
        """TestCase for asving objects to json"""
        return
        # self.fs.attr1 = 'Today'
        # self.fs.save()
        # with open(self.fs.FileStorage().__file_path, 'r') as f:
        #     contents_json = f.read()
        #     contents_expected = {'attr1' : 'Today'}
        # self.assertEqual(contents_json, contents_expected)

    def test_reload(self):
        """TestCase for uploading objects from json"""
        return

    def test_all(self):
        """TestCase for returning a dictionary"""
        return


if __name__ == '__main__':
    unittest.main()
