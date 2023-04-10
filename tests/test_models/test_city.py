#!/usr/bin/python3
"""unittest module for City class
unittest classes:
    Test_City_Instantiation
    TestCityClass
"""
import models
from datetime import datetime
import time
import unittest
from models.city import City
import pycodestyle


class Test_City_Instantiation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ sets up class instance"""
        cls.city = City()

    @classmethod
    def tearDownClass(cls):
        """tear Down Class Instance"""
        del cls.city

    def test_no_arg_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instances_in_objects(self):
        self.assertIn(self.city, models.storage.all().values())

    def test_id(self):
        """test if id is string after is has been
        converted to string in BaseModel()"""
        self.assertEqual(type(self.city.id), str)

    def test_two_users_id_is_unique(self):
        """test if same id occur twice"""
        city2 = City()
        self.assertNotEqual(self.city.id, city2.id)

    def test_updated_at(self):
        """test to comfirm 'updated_at' attribute is a datetime object
        and also not private attr"""
        self.assertEqual(type(self.city.updated_at), datetime)

    def test_created_at(self):
        """confirm if 'created_at' is a public datetime"""
        self.assertEqual(type(self.city.created_at), datetime)

    def test_args_instantiation(self):
        """test to confirm args is unused"""
        City(None)
        self.assertNotIn(None, City().__dict__.values())

    def test_kwargs_instantiation(self):
        """test key word arguments instantiation"""
        dateNtime = datetime.now()
        dateNtime2 = dateNtime.isoformat()
        city = City(id="123", created_at=dateNtime2, updated_at=dateNtime2)
        self.assertEqual(city.id, "123")
        self.assertEqual(city.created_at, dateNtime)
        self.assertEqual(city.updated_at, dateNtime)

    def test_args_kwargs_instantiation(self):
        """test to confirm that BaseModel will discard args
        and make us of the kwargs"""
        date_time = datetime.now()
        formated_date_time = date_time.isoformat()
        city = City("Ajiboye", id="123", created_at=formated_date_time,
                    updated_at=formated_date_time)
        self.assertEqual(city.id, "123")
        self.assertEqual(city.created_at, date_time)
        self.assertEqual(city.updated_at, date_time)

    def test_created_at(self):
        """test two different created_at time"""
        city1 = self.city
        time.sleep(0.5)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_udated_at(self):
        """test two different updated time"""
        city1 = self.city
        time.sleep(0.5)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)


class TestCityClass(unittest.TestCase):
    """Test for BaseModel class attributes and methods"""
    @classmethod
    def setUpClass(cls):
        """Set up class instance"""
        cls.city = City()

    @classmethod
    def tearDownClass(cls):
        del cls.city

    def test_pycodestyle_compliance_user(self):
        """test for PEP8/pycodestyle compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Found errors or warnings")

    def test_save_method(self):
        """Test save method to confirm if updated time changes etc."""
        first_instance = City()
        original_time = first_instance.updated_at
        time.sleep(0.5)
        first_instance.save()
        new_updated_time = first_instance.updated_at
        self.assertNotEqual(original_time, new_updated_time)

    def test_save_with_arg(self):
        self.city
        with self.assertRaises(TypeError):
            self.city.save(None)

    def test_saves_updates_file(self):
        self.city.save()
        Id = "City." + self.city.id
        with open("file.json", 'r') as file:
            self.assertIn(Id, file.read())

    def test_to_dict_method(self):
        """Test to_dict_method whether it return a dict object"""
        new_dict = self.city.to_dict()
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
        self.assertEqual(new_dict['__class__'], 'City')

    def test_dict_new_attributes(self):
        """test that dict contains newly added attributes """
        self.city
        self.city.name = "Holberton"
        self.city.state_id = "123-456-789"
        _dict = self.city.to_dict()
        self.assertIn("name", _dict)
        self.assertIn("state_id", _dict)

    def test_to_dict_with_arg(self):
        self.city
        with self.assertRaises(TypeError):
            self.city.to_dict(None)

    def test_str_overide(self):
        _dict = self.city.__dict__
        expected = "[City] ({}) {}".format(self.city.id, _dict)
        self.assertEqual(expected, str(self.city))

    def test_name_attr(self):
        """checks if name is city public str"""
        self.assertIsInstance(self.city.name, str)

    def test_state_id(self):
        """checks if state_id is city public str"""
        self.assertIsInstance(self.city.state_id, str)

    if '__name__' == '__main__':
        unittest.main()
