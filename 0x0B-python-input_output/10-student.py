#!/usr/bin/python3


"""This module contanis a class Student"""


class Student():
    """A Studnet class"""

    def __init__(self, first_name, last_name, age):
        """Initialize first_name, last_name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        json = {"first_name": self.first_name, "last_name": self.last_name,
                "age": self.age}

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return json
            return {key: val for key, val in json.items() if key in attrs}

        return json
