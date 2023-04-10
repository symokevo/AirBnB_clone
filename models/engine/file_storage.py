#!/usr/bin/python3
""" File storage module """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class FileStorage:
    """ class FileStorage
    Serves as file storage engine

    attrs:
        __file path (str): Name of file path to save object to
        __objects (dict): Dictionary of instantiated keyword argument

    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """  returns the dictionary __objects """
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        to_dict = {}
        for key, obj in FileStorage.__objects.items():
            to_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(to_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                load = json.load(f)
                for key, value in load.items():
                    FileStorage.__objects[key] = eval(
                        value['__class__'])(**value)
        except FileNotFoundError:
            return

    def count(self, cls):
        """
        counts the number of objects in storage
        """
        counter = 0
        for key in models.storage.all().keys():
            if cls in key:
                counter += 1
        return counter
