#!/usr/bin/python3
""" module for the subclass 'review' """
from models.base_model import BaseModel


class Review(BaseModel):
    """ sub class review that inherits from class Basemodel"""
    place_id = ""
    user_id = ""
    text = ""
