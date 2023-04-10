#!/usr/bin/python3
""" module of  the subclass city """
from models.base_model import BaseModel


class City(BaseModel):
    """ subclass city that inherits from Basemodel """
    state_id = ""
    name = ""
