#!/usr/bin/python3
"""unittest module for Place class
unittest classes:
    Test_Place_Instantiation
    TestPlaceClass
"""
import models
from datetime import datetime
import time
import unittest
from models.place import Place
import pycodestyle


class Test_Place_Instantiation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ sets up class instance"""
        cls.pl = Place()

    @classmethod
    def tearDownClass(cls):
        """tear Down Class Instance"""
        del cls.pl

    def test_no_arg_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instances_in_objects(self):
        self.assertIn(self.pl, models.storage.all().values())

    def test_id(self):
        """test if id is string after is has been
        converted to string in BaseModel()"""
        self.assertEqual(type(self.pl.id), str)

    def test_two_users_id_is_unique(self):
        """test if same id occur twice"""
        pl2 = Place()
        self.assertNotEqual(self.pl.id, pl2.id)

    def test_updated_at(self):
        """test to comfirm 'updated_at' atatribute is a datetime object
        and also not private attr"""
        self.assertEqual(type(self.pl.updated_at), datetime)

    def test_created_at(self):
        """confirm if 'created_at' is a public datetime"""
        self.assertEqual(type(self.pl.created_at), datetime)

    def test_args_instantiation(self):
        """test to confirm args is unused"""
        Place(None)
        self.assertNotIn(None, Place().__dict__.values())

    def test_kwargs_instantiation(self):
        """test key word arguments instantiation"""
        dateNtime = datetime.now()
        dateNtime2 = dateNtime.isoformat()
        pls = Place(id="123", created_at=dateNtime2, updated_at=dateNtime2)
        self.assertEqual(pls.id, "123")
        self.assertEqual(pls.created_at, dateNtime)
        self.assertEqual(pls.updated_at, dateNtime)

    def test_args_kwargs_instantiation(self):
        """test to confirm that BaseModel will discard args
        and make us of the kwargs"""
        date_time = datetime.now()
        formated_date_time = date_time.isoformat()
        pls = Place("Ajiboye", id="123", created_at=formated_date_time,
                    updated_at=formated_date_time)
        self.assertEqual(pls.id, "123")
        self.assertEqual(pls.created_at, date_time)
        self.assertEqual(pls.updated_at, date_time)

    def test_created_at(self):
        """test two different created_at time"""
        place1 = self.pl
        time.sleep(0.5)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_udated_at(self):
        """test two different updated time"""
        pl1 = self.pl
        time.sleep(0.5)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)


class TestPlaceClass(unittest.TestCase):
    """Test for BaseModel class attributes and methods"""
    @classmethod
    def setUpClass(cls):
        """Set up class instance"""
        cls.pl = Place()

    @classmethod
    def tearDownClass(cls):
        del cls.pl

    def test_pycodestyle_compliance_user(self):
        """test for PEP8/pycodestyle compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Found errors or warnings")

    def test_save_method(self):
        """Test save method to confirm if updated time changes etc."""
        first_instance = Place()
        original_time = first_instance.updated_at
        time.sleep(0.5)
        first_instance.save()
        new_updated_time = first_instance.updated_at
        self.assertNotEqual(original_time, new_updated_time)

    def test_save_with_arg(self):
        self.pl
        with self.assertRaises(TypeError):
            self.pl.save(None)

    def test_saves_updates_file(self):
        self.pl.save()
        Id = "Place." + self.pl.id
        with open("file.json", 'r') as file:
            self.assertIn(Id, file.read())

    def test_to_dict_method(self):
        """Test to_dict_method whether it return a dict object"""
        new_dict = self.pl.to_dict()
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
        self.assertEqual(new_dict['__class__'], 'Place')

    def test_dict_new_attributes(self):
        """test that dict contains newly added attributes """
        self.pl
        self.pl.name = "Holberton"
        self.pl.state_id = "123-456-789"
        _dict = self.pl.to_dict()
        self.assertIn("name", _dict)
        self.assertIn("state_id", _dict)

    def test_to_dict_with_arg(self):
        self.pl
        with self.assertRaises(TypeError):
            self.pl.to_dict(None)

    def test_str_overide(self):
        _dict = self.pl.__dict__
        expected = "[Place] ({}) {}".format(self.pl.id, _dict)
        self.assertEqual(expected, str(self.pl))

    def test_name_attr(self):
        """checks if name is city public str"""
        self.assertIsInstance(self.pl.name, str)

    def test_user_id(self):
        """checks if state_id is city public str"""
        self.assertIsInstance(self.pl.user_id, str)

    def test_city_id_attr(self):
        """ checks if attr city exists and is public str"""
        self.assertIsInstance(self.pl.city_id, str)

    def test_description_attr(self):
        """checks for description, and is public str"""
        self.assertIsInstance(self.pl.description, str)

    def test_number_rooms_attr(self):
        """check for place number rooms, and is public int"""
        self.assertIsInstance(self.pl.number_rooms, int)

    def test_number_bathrooms(self):
        """checks if number bathrooms --> int"""
        self.assertIsInstance(self.pl.number_bathrooms, int)

    def test_max_guest(self):
        """test maximum guest --> int"""
        self.assertIsInstance(self.pl.max_guest, int)

    def test_price_by_night(self):
        """checks for test by night --> int"""
        self.assertIsInstance(self.pl.price_by_night, int)

    def test_latitude(self):
        """check for latitude --> public float"""
        self.assertIsInstance(self.pl.latitude, float)

    def test_longitude(self):
        """checks for longitude --> public float"""
        self.assertIsInstance(self.pl.longitude, float)

    def test_amenity_ids(self):
        """tests for amenity ids --> list"""
        self.assertIsInstance(self.pl.amenity_ids, list)

    if '__name__' == '__main__':
        unittest.main()
