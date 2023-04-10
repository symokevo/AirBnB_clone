#!/usr/bin/python3
"""unittest module for State class
unittest classes:
    Test_State_Instantiation
    Test_State_Class
"""
import models
from datetime import datetime
import time
import unittest
from models.state import State
import pycodestyle


class Test_State_Instantiation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ sets up class instance"""
        cls.state = State()

    @classmethod
    def tearDownClass(cls):
        """tear Down Class Instance"""
        del cls.state

    def test_no_arg_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instances_in_objects(self):
        self.assertIn(self.state, models.storage.all().values())

    def test_id(self):
        """test if id is string after is has been
        converted to string in BaseModel()"""
        self.assertEqual(type(self.state.id), str)

    def test_two_users_id_is_unique(self):
        """test if same id occur twice"""
        state2 = State()
        self.assertNotEqual(self.state.id, state2.id)

    def test_updated_at(self):
        """test to comfirm 'updated_at' attribute is a datetime object
        and also not private attr"""
        self.assertEqual(type(self.state.updated_at), datetime)

    def test_created_at(self):
        """confirm if 'created_at' is a public datetime"""
        self.assertEqual(type(self.state.created_at), datetime)

    def test_args_instantiation(self):
        """test to confirm args is unused"""
        State(None)
        self.assertNotIn(None, State().__dict__.values())

    def test_kwargs_instantiation(self):
        """test key word arguments instantiation"""
        dateNtime = datetime.now()
        dateNtime2 = dateNtime.isoformat()
        state = State(id="123", created_at=dateNtime2, updated_at=dateNtime2)
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, dateNtime)
        self.assertEqual(state.updated_at, dateNtime)

    def test_args_kwargs_instantiation(self):
        """test to confirm that BaseModel will discard args
        and make us of the kwargs"""
        date_time = datetime.now()
        formated_date_time = date_time.isoformat()
        state = State("Ajiboye", id="123", created_at=formated_date_time,
                      updated_at=formated_date_time)
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, date_time)
        self.assertEqual(state.updated_at, date_time)

    def test_created_at(self):
        """test two different created_at time"""
        state1 = self.state
        time.sleep(0.5)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_udated_at(self):
        """test two different updated time"""
        state1 = self.state
        time.sleep(0.5)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)


class Test_State_Class(unittest.TestCase):
    """Test for BaseModel class attributes and methods"""
    @classmethod
    def setUpClass(cls):
        """Set up class instance"""
        cls.state = State()

    @classmethod
    def tearDownClass(cls):
        del cls.state

    def test_pycodestyle_compliance_user(self):
        """test for PEP8/pycodestyle compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Found errors or warnings")

    def test_save_method(self):
        """Test save method to confirm if updated time changes etc."""
        first_instance = State()
        original_time = first_instance.updated_at
        time.sleep(0.5)
        first_instance.save()
        new_updated_time = first_instance.updated_at
        self.assertNotEqual(original_time, new_updated_time)

    def test_save_with_arg(self):
        self.state
        with self.assertRaises(TypeError):
            self.state.save(None)

    def test_saves_updates_file(self):
        self.state.save()
        Id = "State." + self.state.id
        with open("file.json", 'r') as file:
            self.assertIn(Id, file.read())

    def test_to_dict_method(self):
        """Test to_dict_method whether it return a dict object"""
        new_dict = self.state.to_dict()
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
        self.assertEqual(new_dict['__class__'], 'State')

    def test_dict_new_attributes(self):
        """test that dict contains newly added attributes """
        self.state
        self.state.name = "Holberton School"
        _dict = self.state.to_dict()
        self.assertIn("name", _dict)

    def test_to_dict_with_arg(self):
        self.state
        with self.assertRaises(TypeError):
            self.state.to_dict(None)

    def test_str_overide(self):
        _dict = self.state.__dict__
        expected = "[State] ({}) {}".format(self.state.id, _dict)
        self.assertEqual(expected, str(self.state))

    def test_name_attr(self):
        """checks if name attr exists and is public str"""
        self.assertIsInstance(self.state.name, str)

    if '__name__' == '__main__':
        unittest.main()
