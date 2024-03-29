#!/usr/bin/python3
"""This module contains "Base" Class """

import json
import csv
import turtle


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
        if dictionary is None or dictionary == {}:
            return None
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the Rectangles and Squares using Turtle graphics module"""

        t = turtle.Turtle()
        t.speed(1)
        t.shape("turtle")
        t.pensize(3)
        t.color((41, 256, 256))
        for rec in list_rectangles:
            t.pu()
            t.goto(rec.x, rec.y)
            t.right(0)
            t.pd()
            t.fd(rec.width)
            t.left(90)
            t.color("red")
            t.fd(rec.height)
            t.left(90)
            t.color((41, 41, 253))
            t.fd(rec.width)
            t.left(90)
            t.color(41, 253, 41)
            t.fd(sq.height)
            t.left(90)
            t.color((41, 256, 256))

        for sq in list_squares:
            t.pu()
            t.goto(sq.x, sq.y)
            t.right(0)
            t.pd()
            t.fd(sq.width)
            t.left(90)
            t.color("red")
            t.fd(sq.height)
            t.left(90)
            t.color((41, 41, 253))
            t.fd(sq.width)
            t.left(90)
            t.color(41, 253, 41)
            t.fd(sq.height)
            t.left(90)
            t.color((41, 256, 256))

        turtle.exitonclick()
