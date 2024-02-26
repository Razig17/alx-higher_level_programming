#!/usr/bin/python3
"""This module contains "Base" Class """

import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries:"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is not None and list_objs != []:
            json_ls = [obj.to_dictionary() for obj in list_objs]
        else:
            json_ls = []
        name = cls.__name__ + ".json"
        with open(name, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(json_ls))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary is None or len(dictionary) == 0:
            return None
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file"""
        try:
            with open(f"{cls.__name__}.json", "r", encoding="UTF8") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
