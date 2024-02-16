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
        if list_objs is None:
            list_objs = []

        field_obj = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.json".format(cls.__name__)
        json_string = cls.to_json_string(field_obj)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """adding static method that returns list of JSON str"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Classmethod that returns all attributes set"""
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """load files that returns list of instances"""
        filename = "{}.json".format(cls.__name__)
        if not filename:
            return "[]"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                inst_data = cls.from_json_string(json_data)
                return [cls.create(**inst) for inst in inst_data]
        except FileNotFoundError:
            return []
