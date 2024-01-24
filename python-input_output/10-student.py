#!/usr/bin/python3
"""Write a class student that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of a student"""
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)}
