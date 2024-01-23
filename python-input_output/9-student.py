#!/usr/bin/python3
"""Define a stdent class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """ Publice attributes:"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve dictionary representation"""
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
