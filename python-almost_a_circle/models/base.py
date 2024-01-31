#!/usr/bin/python3
"""First class Base and attribute"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returning JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of list_objs to file"""
        if list_obj is None:
            list_objs = []

        field_objects = [obj.to_dict() for obj in list_objs]
        filename = "output.json"

        with open(filename, 'w') as file:
            json.dump(field_objects, file)
