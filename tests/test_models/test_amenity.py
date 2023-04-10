#!/usr/bin/python3
"""unittest module for Amenity class

Test classes:
    TestAmenity_Instantiation
    TestAmenityClass
    """
import models
from datetime import datetime
import time
import unittest
from models.amenity import Amenity
import pycodestyle


class TestAmenity_Instantiation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ sets up class instance"""
        cls.amenity = Amenity()

    @classmethod
    def tearDownClass(cls):
        """tear Down Class Instance"""
        del cls.amenity

    def test_no_arg_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instances_in_objects(self):
        self.assertIn(self.amenity, models.storage.all().values())

    def test_id(self):
        """test if id is string after is has been
        converted to string in BaseModel()"""
        self.assertEqual(type(self.amenity.id), str)

    def test_two_users_id_is_unique(self):
        """test if same id occur twice"""
        amenity2 = Amenity()
        self.assertNotEqual(self.amenity.id, amenity2.id)

    def test_updated_at(self):
        """test to comfirm 'updated_at' attribute is a datetime object
        and also not private attr"""
        self.assertEqual(type(self.amenity.updated_at), datetime)

    def test_created_at(self):
        """confirm if 'created_at' is a public datetime"""
        self.assertEqual(type(self.amenity.created_at), datetime)

    def test_args_instantiation(self):
        """test to confirm args is unused"""
        Amenity(None)
        self.assertNotIn(None, Amenity().__dict__.values())

    def test_kwargs_instantiation(self):
        """test key word arguments instantiation"""
        dateNtime = datetime.now()
        dateNtime2 = dateNtime.isoformat()
        amenity = Amenity(id="123", created_at=dateNtime2,
                          updated_at=dateNtime2)
        self.assertEqual(amenity.id, "123")
        self.assertEqual(amenity.created_at, dateNtime)
        self.assertEqual(amenity.updated_at, dateNtime)

    def test_args_kwargs_instantiation(self):
        """test to confirm that BaseModel will discard args
        and make us of the kwargs"""
        date_time = datetime.now()
        formated_date_time = date_time.isoformat()
        amenity = Amenity("Ajiboye", id="123", created_at=formated_date_time,
                          updated_at=formated_date_time)
        self.assertEqual(amenity.id, "123")
        self.assertEqual(amenity.created_at, date_time)
        self.assertEqual(amenity.updated_at, date_time)

    def test_created_at(self):
        """test two different created_at time"""
        amenity1 = self.amenity
        time.sleep(0.5)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_udated_at(self):
        """test two different updated time"""
        amenity1 = self.amenity
        time.sleep(0.5)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)


class TestAmenityClass(unittest.TestCase):
    """Test for BaseModel class attributes and methods"""
    @classmethod
    def setUpClass(cls):
        """Set up class instance"""
        cls.amenity = Amenity()

    @classmethod
    def tearDownClass(cls):
        del cls.amenity

    def test_pycodestyle_compliance_user(self):
        """test for PEP8/pycodestyle compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found errors or warnings")

    def test_save_method(self):
        """Test save method to confirm if updated time changes etc."""
        first_instance = Amenity()
        original_time = first_instance.updated_at
        time.sleep(0.5)
        first_instance.save()
        new_updated_time = first_instance.updated_at
        self.assertNotEqual(original_time, new_updated_time)

    def test_save_with_arg(self):
        self.amenity
        with self.assertRaises(TypeError):
            self.amenity.save(None)

    def test_saves_updates_file(self):
        self.amenity.save()
        Id = "Amenity." + self.amenity.id
        with open("file.json", 'r') as file:
            self.assertIn(Id, file.read())

    def test_to_dict_method(self):
        """Test to_dict_method whether it return a dict object"""
        new_dict = self.amenity.to_dict()
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
        self.assertEqual(new_dict['__class__'], 'Amenity')

    def test_dict_new_attributes(self):
        """test that dict contains newly added attributes """
        self.amenity
        self.amenity.name = "Holberton School"
        _dict = self.amenity.to_dict()
        self.assertIn("name", _dict)

    def test_to_dict_with_arg(self):
        self.amenity
        with self.assertRaises(TypeError):
            self.amenity.to_dict(None)

    def test_str_overide(self):
        _dict = self.amenity.__dict__
        expected = "[Amenity] ({}) {}".format(self.amenity.id, _dict)
        self.assertEqual(expected, str(self.amenity))

    def test_name_attr(self):
        """checks if name attr exists and is public str"""
        self.assertIsInstance(self.amenity.name, str)

    if '__name__' == '__main__':
        unittest.main()
