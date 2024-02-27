#!/usr/bin/python3

"""Unittest module for class Base"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Unit test for base class"""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_two_bases(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_unique_id(self):
        self.assertEqual(Base(7).id, 7)

    def test_id_after_unique(self):
        base1 = Base()
        base2 = Base(7)
        base3 = Base()
        self.assertEqual(base1.id + 1, base3.id)

    def test_None(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_list_id(self):
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_str_id(self):
        self.assertEqual(Base("test").id, "test")

    def test_negative_id(self):
        self.assertEqual(Base(-5).id, -5)

    def test_private_attribute(self):
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects())
    
    def test_changing_id(self):
        b1 = Base(20)
        b1.id = 25
        self.assertEqual(b1.id, 25)

    def test_to_json_string(self):
        d = Rectangle(3, 5, 7, 9, 10).to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([d])))

    def test_to_json_rectangle_two_dict(self):
        d1 = Rectangle(3, 5, 7, 9, 10).to_dictionary()
        d2 = Rectangle(2, 4, 6, 8, 11).to_dictionary()
        self.assertEqual([d1, d2], eval((Base.to_json_string([d1, d2]))))
        self.assertTrue(len(Base.to_json_string([d1, d2])) == 106)

    def test_to_json_square(self):
        d = Square(3, 7, 9, 10).to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([d])))

    def test_to_json_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 2)

    def test_save_to_file_rectangle(self):
        r = Rectangle(3, 5, 7, 9, 10)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 53)
    
    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(3, 5, 7, 9, 10)
        r2 = Rectangle(2, 4, 6, 8, 11)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 106)

    def test_save_to_file_one_square(self):
        s = Square(3, 7, 9, 10)
        Square.save_to_file([s])
        with open("Square.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(3, 7, 9, 10)
        s2 = Square(2, 6, 8, 11)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 78)

    def test_save_to_file_class_name(self):
        s = Square(3, 7, 9, 10)
        Base.save_to_file([s])
        with open("Base.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 39)

    def test_save_to_file_overwrite(self):
        s1 = Square(3, 7, 9, 10)
        Square.save_to_file([s1])
        s2 = Square(2, 6, 8, 11)
        Square.save_to_file([s2])
        with open("Square.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 39)

    def test_base_save_to_file_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r", encoding="UTF8") as f:
            self.assertEqual(f.read(), "[]")

    def test_base_to_file_None(self):
        Base.save_to_file(None)
        with open("Base.json", "r", encoding="UTF8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_no_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()
    
    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file([], 2)

    def test_from_json_string_type(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_two_rectangle(self):
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list_input, list_output)


    def test_from_json_string_two_squares(self):
        list_input = [
                {'id': 89, 'size': 10, 'x': 4},
                {'id': 7, 'size': 1, 'x': 7}
                ]
        json_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_rectangle(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_no_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 2)

    def test_create(self):
        rectangle_dict = {'id': 3, 'width': 6, 'height': 4, 'x': 1, 'y': 2}
        square_dict = {'id': 4, 'size': 3, 'x': 0, 'y': 1}

        created_rectangle = Rectangle.create(**rectangle_dict)
        created_square = Square.create(**square_dict)

        self.assertIsInstance(created_rectangle, Rectangle)
        self.assertIsInstance(created_square, Square)

        self.assertEqual(created_rectangle.id, 3)
        self.assertEqual(created_rectangle.width, 6)
        self.assertEqual(created_square.size, 3)
        self.assertEqual(created_square.y, 1)

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 7, 9, 11)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (11) 7/9 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 7, 9, 11)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (11) 7/9 - 3/5", str(r1))
    
    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 7, 9, 11)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)




if __name__ == "__main__":
    unittest.main()