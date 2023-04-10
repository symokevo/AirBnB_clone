#!/usr/bin/python3
"""unittest module for Review class
unittest classes:
    Test_Review_Instantiation
    TestReviewClass
"""
import models
from datetime import datetime
import time
import unittest
from models.review import Review
import pycodestyle


class Test_Review_Instantiation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ sets up class instance"""
        cls.rw = Review()

    @classmethod
    def tearDownClass(cls):
        """tear Down Class Instance"""
        del cls.rw

    def test_no_arg_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instances_in_objects(self):
        self.assertIn(self.rw, models.storage.all().values())

    def test_id(self):
        """test if id is string after is has been
        converted to string in BaseModel()"""
        self.assertEqual(type(self.rw.id), str)

    def test_two_users_id_is_unique(self):
        """test if same id occur twice"""
        rw2 = Review()
        self.assertNotEqual(self.rw.id, rw2.id)

    def test_updated_at(self):
        """test to comfirm 'updated_at' attribute is a datetime object
        and also not private attr"""
        self.assertEqual(type(self.rw.updated_at), datetime)

    def test_created_at(self):
        """confirm if 'created_at' is a public datetime"""
        self.assertEqual(type(self.rw.created_at), datetime)

    def test_args_instantiation(self):
        """test to confirm args is unused"""
        Review(None)
        self.assertNotIn(None, Review().__dict__.values())

    def test_kwargs_instantiation(self):
        """test key word arguments instantiation"""
        dateNtime = datetime.now()
        dateNtime2 = dateNtime.isoformat()
        rw = Review(id="123", created_at=dateNtime2, updated_at=dateNtime2)
        self.assertEqual(rw.id, "123")
        self.assertEqual(rw.created_at, dateNtime)
        self.assertEqual(rw.updated_at, dateNtime)

    def test_args_kwargs_instantiation(self):
        """test to confirm that BaseModel will discard args
        and make us of the kwargs"""
        date_time = datetime.now()
        formated_date_time = date_time.isoformat()
        rw = Review("Ajiboye", id="123", created_at=formated_date_time,
                    updated_at=formated_date_time)
        self.assertEqual(rw.id, "123")
        self.assertEqual(rw.created_at, date_time)
        self.assertEqual(rw.updated_at, date_time)

    def test_created_at(self):
        """test two different created_at time"""
        rw1 = self.rw
        time.sleep(0.5)
        rw2 = Review()
        self.assertLess(rw1.created_at, rw2.created_at)

    def test_udated_at(self):
        """test two different updated time"""
        rw1 = self.rw
        time.sleep(0.5)
        rw2 = Review()
        self.assertLess(rw1.updated_at, rw2.updated_at)


class TestReviewClass(unittest.TestCase):
    """Test for BaseModel class attributes and methods"""
    @classmethod
    def setUpClass(cls):
        """Set up class instance"""
        cls.rw = Review()

    @classmethod
    def tearDownClass(cls):
        del cls.rw

    def test_pycodestyle_compliance_user(self):
        """test for PEP8/pycodestyle compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Found errors or warnings")

    def test_save_method(self):
        """Test save method to confirm if updated time changes etc."""
        first_instance = Review()
        original_time = first_instance.updated_at
        time.sleep(0.5)
        first_instance.save()
        new_updated_time = first_instance.updated_at
        self.assertNotEqual(original_time, new_updated_time)

    def test_save_with_arg(self):
        self.rw
        with self.assertRaises(TypeError):
            self.rw.save(None)

    def test_saves_updates_file(self):
        self.rw.save()
        Id = "Review." + self.rw.id
        with open("file.json", 'r') as file:
            self.assertIn(Id, file.read())

    def test_to_dict_method(self):
        """Test to_dict_method whether it return a dict object"""
        new_dict = self.rw.to_dict()
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
        self.assertEqual(new_dict['__class__'], 'Review')

    def test_dict_new_attributes(self):
        """test that dict contains newly added attributes """
        self.rw
        self.rw.name = "Holberton School"
        _dict = self.rw.to_dict()
        self.assertIn("name", _dict)

    def test_to_dict_with_arg(self):
        self.rw
        with self.assertRaises(TypeError):
            self.rw.to_dict(None)

    def test_str_overide(self):
        _dict = self.rw.__dict__
        expected = "[Review] ({}) {}".format(self.rw.id, _dict)
        self.assertEqual(expected, str(self.rw))

    def test_place_id_attr(self):
        """checks if place_id attr exists --> public str"""
        self.assertIsInstance(self.rw.place_id, str)

    def test_user_id(self):
        """test Review public attr user_id"""
        self.assertIsInstance(self.rw.user_id, str)

    def test_text(self):
        """test Review public attr text"""
        self.assertIsInstance(self.rw.text, str)

    if '__name__' == '__main__':
        unittest.main()
