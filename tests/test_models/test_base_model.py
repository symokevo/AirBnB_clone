#!/usr/bin/python3
"""unittest module for basemodel class
unittest classes:
    TestBase_Instantiation
    TestBaseClass
    """
import models
from datetime import datetime
import time
import unittest
from models.base_model import BaseModel
import pycodestyle


class TestBase_Instantiation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ sets up class instance"""
        cls.bm = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """tear Down Class Instance"""
        del cls.bm

    def test_base_model_type(self):
        self.assertEqual(BaseModel, type(self.bm))

    def test_new_instances_in_objects(self):
        self.assertIn(self.bm, models.storage.all().values())

    def test_id(self):
        """test if id is string after is has been
        converted to string in BaseModel()"""
        self.assertEqual(type(self.bm.id), str)

    def test_id_is_unique(self):
        """test if same id occur twice"""
        bm2 = BaseModel()
        self.assertNotEqual(self.bm.id, bm2.id)

    def test_updated_at(self):
        """test to comfirm 'updated_at' attribute is a datetime object
        and also not private attr"""
        self.assertEqual(type(self.bm.updated_at), datetime)

    def test_created_at(self):
        """confirm if 'created_at' is a public datetime"""
        self.assertEqual(type(self.bm.created_at), datetime)

    def test_args_instantiation(self):
        """test to confirm args is unused"""
        BaseModel(None)
        self.assertNotIn(None, BaseModel.__dict__.values())

    def test_kwargs_instantiation(self):
        """test key word arguments instantiation"""
        dateNtime = datetime.now()
        dateNtime2 = dateNtime.isoformat()
        bm = BaseModel(id="123", created_at=dateNtime2, updated_at=dateNtime2)
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at, dateNtime)
        self.assertEqual(bm.updated_at, dateNtime)

    def test_args_kwargs_instantiation(self):
        """test to confirm that BaseModel will discard args
        and make us of the kwargs"""
        date_time = datetime.now()
        formated_date_time = date_time.isoformat()
        bm = BaseModel("Ajiboye", id="123", created_at=formated_date_time,
                       updated_at=formated_date_time)
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at, date_time)
        self.assertEqual(bm.updated_at, date_time)

    def test_created_at(self):
        """test two different created_at time"""
        bm1 = self.bm
        time.sleep(0.5)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_udated_at(self):
        """test two different updated time"""
        bm1 = self.bm
        time.sleep(0.5)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)


class TestBaseClass(unittest.TestCase):
    """Test for BaseModel class attributes and methods"""
    @classmethod
    def setUpClass(cls):
        """Set up class instance"""
        cls.testbase = BaseModel()

    @classmethod
    def tearDownClass(cls):
        del cls.testbase

    def test_pycodestyle_compliance_base_model(self):
        """test for PEP8/pycodestyle compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found errors or warnings")

    def test_save_method(self):
        """Test save method to confirm if updated time changes etc."""
        first_instance = BaseModel()
        original_time = first_instance.updated_at
        time.sleep(0.5)
        first_instance.save()
        new_updated_time = first_instance.updated_at
        self.assertNotEqual(original_time, new_updated_time)

    def test_save_with_arg(self):
        self.testbase
        with self.assertRaises(TypeError):
            self.testbase.save(None)

    def test_saves_updates_file(self):
        self.testbase.save()
        Id = "BaseModel." + self.testbase.id
        with open("file.json", 'r') as file:
            self.assertIn(Id, file.read())

    def test_to_dict_method(self):
        """Test to_dict_method whether it return a dict object"""
        new_dict = self.testbase.to_dict()
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
        self.assertEqual(new_dict['__class__'], 'BaseModel')

    def test_dict_new_attributes(self):
        """test that dict contains newly added attributes """
        self.testbase
        self.testbase.name = "Holberton_School"
        self.testbase.my_number = 98
        _dict = self.testbase.to_dict()
        self.assertIn("name", _dict)
        self.assertIn("my_number", _dict)

    def test_to_dict_with_arg(self):
        self.testbase
        with self.assertRaises(TypeError):
            self.testbase.to_dict(None)

    def test_str_overide(self):
        _dict = self.testbase.__dict__
        expected = "[BaseModel] ({}) {}".format(self.testbase.id, _dict)
        self.assertEqual(expected, str(self.testbase))

    if '__name__' == '__main__':
        unittest.main()
