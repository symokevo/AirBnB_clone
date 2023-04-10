#!/usr/bin/python3
from models.base_model import BaseModel
""" subclass User module """


class User(BaseModel):
    """ subclass user that inherits from Basemodel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
