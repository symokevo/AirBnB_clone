#!/usr/bin/python3
"""unittest module for User class
unittest classes:
    TestUser_Instantiation
    TestUserClass
"""
import models
from datetime import datetime
import time
import unittest
from models.user import User
import pycodestyle


class TestUser_Instantiation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ sets up class instance"""
        cls.user = User()

    @classmethod
    def tearDownClass(cls):
        """tear Down Class Instance"""
        del cls.user

    def test_no_arg_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instances_in_objects(self):
        self.assertIn(self.user, models.storage.all().values())

    def test_id(self):
        """test if id is string after is has been
        converted to string in BaseModel()"""
        self.assertEqual(type(self.user.id), str)

    def test_two_users_id_is_unique(self):
        """test if same id occur twice"""
        user2 = User()
        self.assertNotEqual(self.user.id, user2.id)

    def test_updated_at(self):
        """test to comfirm 'updated_at' attribute is a datetime object
        and also not private attr"""
        self.assertEqual(type(self.user.updated_at), datetime)

    def test_created_at(self):
        """confirm if 'created_at' is a public datetime"""
        self.assertEqual(type(self.user.created_at), datetime)

    def test_args_instantiation(self):
        """test to confirm args is unused"""
        User(None)
        self.assertNotIn(None, User().__dict__.values())

    def test_kwargs_instantiation(self):
        """test key word arguments instantiation"""
        dateNtime = datetime.now()
        dateNtime2 = dateNtime.isoformat()
        user = User(id="123", created_at=dateNtime2, updated_at=dateNtime2)
        self.assertEqual(user.id, "123")
        self.assertEqual(user.created_at, dateNtime)
        self.assertEqual(user.updated_at, dateNtime)

    def test_args_kwargs_instantiation(self):
        """test to confirm that BaseModel will discard args
        and make us of the kwargs"""
        date_time = datetime.now()
        formated_date_time = date_time.isoformat()
        user = User("Ajiboye", id="123", created_at=formated_date_time,
                    updated_at=formated_date_time)
        self.assertEqual(user.id, "123")
        self.assertEqual(user.created_at, date_time)
        self.assertEqual(user.updated_at, date_time)

    def test_created_at(self):
        """test two different created_at time"""
        user1 = self.user
        time.sleep(0.5)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_udated_at(self):
        """test two different updated time"""
        user1 = self.user
        time.sleep(0.5)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)


class TestUserClass(unittest.TestCase):
    """Test for BaseModel class attributes and methods"""
    @classmethod
    def setUpClass(cls):
        """Set up class instance"""
        cls.user = User()

    @classmethod
    def tearDownClass(cls):
        del cls.user

    def test_pycodestyle_compliance_user(self):
        """test for PEP8/pycodestyle compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Found errors or warnings")

    def test_save_method(self):
        """Test save method to confirm if updated time changes etc."""
        first_instance = User()
        original_time = first_instance.updated_at
        time.sleep(0.5)
        first_instance.save()
        new_updated_time = first_instance.updated_at
        self.assertNotEqual(original_time, new_updated_time)

    def test_save_with_arg(self):
        self.user
        with self.assertRaises(TypeError):
            self.user.save(None)

    def test_saves_updates_file(self):
        self.user.save()
        Id = "User." + self.user.id
        with open("file.json", 'r') as file:
            self.assertIn(Id, file.read())

    def test_to_dict_method(self):
        """Test to_dict_method whether it return a dict object"""
        new_dict = self.user.to_dict()
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
        self.assertEqual(new_dict['__class__'], 'User')

    def test_dict_new_attributes(self):
        """test that dict contains newly added attributes """
        self.user
        self.user.first_name = "Holberton"
        self.user.email = "Alx@alx.com"
        self.user.password = "$12345!"
        self.user.last_name = "School"
        self.user.my_number = 98
        _dict = self.user.to_dict()
        self.assertIn("first_name", _dict)
        self.assertIn("my_number", _dict)
        self.assertIn("password", _dict)
        self.assertIn("last_name", _dict)
        self.assertIn("email", _dict)

    def test_to_dict_with_arg(self):
        self.user
        with self.assertRaises(TypeError):
            self.user.to_dict(None)

    def test_str_overide(self):
        _dict = self.user.__dict__
        expected = "[User] ({}) {}".format(self.user.id, _dict)
        self.assertEqual(expected, str(self.user))

    def test_email_attribute(self):
        """checks if email is str"""
        self.assertIsInstance(self.user.email, str)

    def test_first_name_attr(self):
        """checks if first name is public str"""
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_attr(self):
        """checks if last name is public str"""
        self.assertIsInstance(self.user.last_name, str)

    def test_password_attr(self):
        """checks if password is public str"""
        self.assertIsInstance(self.user.password, str)

    if '__name__' == '__main__':
        unittest.main()
