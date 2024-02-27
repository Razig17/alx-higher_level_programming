#!/usr/bin/python3

"""Unittest module for class Rectangle"""

import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle



class TestRectangleClass(unittest.TestCase):
    """Unit test for Rectangle class"""


    @staticmethod
    def capture_from_stdout(rect, method):
        """Capture the output from the stdout to use it in testing"""
        capture = StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        elif method == "display":
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_is_a_child(self):
        self.assertIsInstance(Rectangle(5, 6), Base)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_two_rectangles(self):
        r1 = Rectangle(2, 4)
        r2 = Rectangle(5, 6)
        self.assertEqual(r1.id, r2.id - 1)
    
    def test_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__width
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__height
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__x
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__y
    
    def test_width_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.width = 6
        self.assertEqual(r1.width, 6)

    def test_height_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.height, 4)

    def test_width_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.height = 6
        self.assertEqual(r1.height, 6)

    def test_x_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.x, 6)

    def test_x_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.x = 5
        self.assertEqual(r1.x, 5)

    def test_y_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.y, 8)

    def test_y_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.y = 6
        self.assertEqual(r1.y, 6)
    
    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.3, 5)

    def test_NaN_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 5)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 5)

    def test_small_area(self):
        self.assertEqual(Rectangle(3, 5).area(), 15)

    def test_large_area(self):
        a1 = Rectangle(9999999999, 9999999999).area()
        self.assertEqual(a1, 99999999980000000001)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            a1 = Rectangle(3, 5).area(3)

    def test_attribute_changed(self):
        r1 = Rectangle(3, 5)
        r1.height = 3
    
    def test_display_width_height(self):
        r = Rectangle(2, 4)
        output = self.capture_from_stdout(r, "display").getvalue()
        self.assertEqual("##\n##\n##\n##\n", output)

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 1, 2)
        output = self.capture_from_stdout(r, "display").getvalue()
        self.assertEqual("\n\n ##\n ##\n ##\n ##\n", output)

    def test_display_changed_attribute(self):
        r = Rectangle(2, 4)
        r.width = 3
        r.height = 3
        output = self.capture_from_stdout(r, "display").getvalue()
        self.assertEqual("###\n###\n###\n", output)

    def test_display_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).display(3)

    def test_str_print(self):
        r = Rectangle(2, 4)
        actual = self.capture_from_stdout(r, "print").getvalue()
        expected = "[Rectangle] ({}) 0/0 - 2/4\n".format(r.id)
        self.assertEqual(expected, actual)

    def test_str_width_height_x_y(self):
        r = Rectangle(2, 4, 6, 8)
        self.assertEqual("[Rectangle] ({}) 6/8 - 2/4".format(r.id), str(r))

    def test_str_width_height_x_y_id(self):
        r = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual("[Rectangle] (10) 6/8 - 2/4", str(r))

    def test_str_changed_attribute(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.width = 3
        r.height = 3
        self.assertEqual("[Rectangle] (10) 6/8 - 3/3", str(r))

    def test_str_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 5).__str__(1)

    def test_update_no_args(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 6/8 - 2/4", str(r))

    def test_update_one_arg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(12)
        self.assertEqual("[Rectangle] (12) 6/8 - 2/4", str(r))

    def test_update_four_args(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(12, 5, 7, 9)
        self.assertEqual("[Rectangle] (12) 9/8 - 5/7", str(r))

    def test_update_five_args(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(12, 5, 7, 9, 11)
        self.assertEqual("[Rectangle] (12) 9/11 - 5/7", str(r))

    def test_update_more_than_five_args(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(12, 5, 7, 9, 11, 13)
        self.assertEqual("[Rectangle] (12) 9/11 - 5/7", str(r))

    def test_update_with_None(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(None)
        self.assertEqual("[Rectangle] ({}) 6/8 - 2/4".format(r.id), str(r))

    def test_update_with_None_and_more(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(None, 3, 5, 7)
        self.assertEqual("[Rectangle] ({}) 7/8 - 3/5".format(r.id), str(r))

    def test_update_invalid_width_type(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(12, "invalid width")

    def test_update_width_zero(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(12, 0)

    def test_update_width_negative(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(12, -3)
    
    def test_update_id_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(id=3)
        self.assertEqual("[Rectangle] (3) 6/8 - 2/4", str(r))

    def test_update_height_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(height=3)
        self.assertEqual("[Rectangle] (10) 6/8 - 2/3", str(r))

    def test_update_width_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(width=3)
        self.assertEqual("[Rectangle] (10) 6/8 - 3/4", str(r))

    def test_update_x_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(x=3)
        self.assertEqual("[Rectangle] (10) 3/8 - 2/4", str(r))

    def test_update_y_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(y=3)
        self.assertEqual("[Rectangle] (10) 6/3 - 2/4", str(r))

    def test_update_five_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(width=3, height=5, x=7, y=9)
        self.assertEqual("[Rectangle] (10) 7/9 - 3/5", str(r))

    def test_update_None_id_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(id=None)
        self.assertEqual("[Rectangle] ({}) 6/8 - 2/4".format(r.id), str(r))

    def test_update_invalid_width_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid width")

    def test_update_zero_width_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)
    
    def test_dictionary_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 5).to_dictionary(3)

    def test_to_dict_output(self):
        actual = Rectangle(10, 2, 1, 9, 1).to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(actual, expected)

    def test_to_dict_changed_attribute(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(3, 5, 7)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())


if __name__ == "__main__":
    unittest.main()