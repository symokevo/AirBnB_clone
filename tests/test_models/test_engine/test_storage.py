#!/usr/bin/python3
"""test module for the file storage class"""
import json
from unittest import TestCase
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorageClass(TestCase):
    """Test for FileStorage class methods and atrributes"""

    @classmethod
    def setUpClass(self):
        """sets up class instance"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def test_storage_methods(self):
        """tests all the 'FileStorage' methods"""
        sto = FileStorage()
        obj = BaseModel()
        sto.new(obj)
        sto.save()
        sto.reload()
        new_dict1 = sto.all()
        new_dict2 = sto.all()
        self.assertEqual(new_dict1, new_dict2)

    @classmethod
    def tearDownClass(self):
        """ tear down the created class instance """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}


    if '__name__' == '__main__':
        unittest.main()
