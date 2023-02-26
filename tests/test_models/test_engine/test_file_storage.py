#!/usr/bin/python3
"""
Contains FileStorage test cases.
"""

import unittest
import os
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines test cases for FileStorage"""

    def test_storage(self):
        """storage should be a FileStorage."""

        self.assertIsInstance(storage, FileStorage)

    def test_new_base_model(self):
        """It should add new BaseModel object to storage."""

        model = BaseModel()
        storage.new(model)
        key = "BaseModel.{}".format(model.id)
        stored_model = storage.all().get(key)
        self.assertEqual(model, stored_model)
        self.assertIsInstance(stored_model, BaseModel)

    def test_new_user(self):
        """It should add new User object to storage."""

        model = User()
        storage.new(model)
        key = "User.{}".format(model.id)
        stored_model = storage.all().get(key)
        self.assertEqual(model, stored_model)
        self.assertIsInstance(stored_model, User)

    def test_new_place(self):
        """It should add new Place object to storage."""

        model = Place()
        storage.new(model)
        key = "Place.{}".format(model.id)
        stored_model = storage.all().get(key)
        self.assertEqual(model, stored_model)
        self.assertIsInstance(stored_model, Place)

    def test_new_state(self):
        """It should add new State object to storage."""

        model = State()
        storage.new(model)
        key = "State.{}".format(model.id)
        stored_model = storage.all().get(key)
        self.assertEqual(model, stored_model)
        self.assertIsInstance(stored_model, State)

    def test_new_city(self):
        """It should add new City object to storage."""

        model = City()
        storage.new(model)
        key = "City.{}".format(model.id)
        stored_model = storage.all().get(key)
        self.assertEqual(model, stored_model)
        self.assertIsInstance(stored_model, City)

    def test_new_amenity(self):
        """It should add new Amenity object to storage."""

        model = Amenity()
        storage.new(model)
        key = "Amenity.{}".format(model.id)
        stored_model = storage.all().get(key)
        self.assertEqual(model, stored_model)
        self.assertIsInstance(stored_model, Amenity)

    def test_new_review(self):
        """It should add new Review object to storage."""

        model = Review()
        storage.new(model)
        key = "Review.{}".format(model.id)
        stored_model = storage.all().get(key)
        self.assertEqual(model, stored_model)
        self.assertIsInstance(stored_model, Review)

    def test_new_other_objs(self):
        """It should not add object to storage for none BaseModel objects."""

        old_size = len(storage.all())
        storage.new(None)
        storage.new(1)
        storage.new(1.5)
        storage.new((1,))
        storage.new([])
        storage.new([1, 2, 3, 4])
        storage.new([1.0, 2.0, 3.0, 4.])
        storage.new({})
        storage.new({'name': "jude"})
        storage.new({'name': "jude", 'age': 27})
        storage.new(True)
        storage.new(False)
        storage.new("")
        new_size = len(storage.all())
        self.assertEqual(old_size, new_size)

    def test_all(self):
        """It should return all objects stored in __objects."""

        objects = storage.all()
        self.assertIsInstance(objects, dict)
        for key in objects:
            obj = objects[key]
            self.assertTrue(issubclass(type(obj), BaseModel))

    def test_save(self):
        """It should save __objects to file.json"""

        my_model = BaseModel()
        my_model.name = "Test"
        my_model.magic = 101
        my_model.save()
        self.assertTrue(os.path.exists("file.json"))
        storage.reload()
        key = "BaseModel.{}".format(my_model.id)
        storedModel = storage.all().get(key, None)
        self.assertIsNotNone(storedModel)

    def test_save_user(self):
        """It should save user __objects to file.json"""

        model = User()
        model.first_name = "Betty"
        model.last_name = "Butter"
        model.save()
        self.assertTrue(os.path.exists("file.json"))
        storage.reload()
        key = "User.{}".format(model.id)
        storedModel = storage.all().get(key, None)
        self.assertIsNotNone(storedModel)

    def test_reload(self):
        """It should reload objects from file.json into __objects"""

        storage.reload()
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        for key in objects:
            obj = objects[key]
            self.assertTrue(issubclass(type(obj), BaseModel))

    def test_reload_error(self):
        """tests reload with arg"""
        with self.assertRaises(ValueError) as context:
            storage.reload("me")


if __name__ == "__main__":
    unittest.main(TestFileStorage)
