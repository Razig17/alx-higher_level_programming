#!/usr/bin/python3

"""Unittest module for class Square"""

import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Unit test for Square class"""

    @staticmethod
    def capture_from_stdout(square, method):
        """Capture the output from the stdout to use it in testing"""
        capture = StringIO()
        sys.stdout = capture
        if method == "print":
            print(square)
        elif method == "display":
            square.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_is_a_child(self):
        self.assertIsInstance(Square(5), Base)
        self.assertIsInstance(Square(5), Rectangle)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(5)
        s2 = Square(6)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.id, 4)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 20)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            Square(1, 4, 3, 5).__size

    def test_size_getter(self):
        s1 = Square(2, 4, 6, 8)
        self.assertEqual(s1.size, 2)

    def test_size_setter(self):
        s1 = Square(2, 4, 6, 8)
        s1.size = 6
        self.assertEqual(s1.size, 6)

    def test_setter(self):
        s1 = Square(2, 4, 6, 8)
        s1.width = 6
        self.assertEqual(s1.width, 6)
        s1 = Square(2, 4, 6, 8)
        s1.y = 3
        self.assertEqual(s1.y, 3)
        s1 = Square(2, 4, 6, 8)
        s1.x = 5
        self.assertEqual(s1.x, 5)
        s1 = Square(2, 4, 6, 8)
        s1.height = 6
        self.assertEqual(s1.height, 6)
        s1 = Square(2, 4, 6, 8)
        s1.width = 6
        self.assertEqual(s1.width, 6)
    
    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(9.9)

    def test_NaN_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b"invalid size")
    
    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-999)

    def test_small_area(self):
        self.assertEqual(Square(3).area(), 9)

    def test_large_area(self):
        a1 = Square(9999999999).area()
        self.assertEqual(a1, 99999999980000000001)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            a1 = Square(3).area(3)

    def test_attribute_changed(self):
        s1 = Square(3)
        s1.size = 5
        self.assertEqual(s1.area(), 25)

    def test_display_size(self):
        s = Square(2)
        output = self.capture_from_stdout(s, "display").getvalue()
        self.assertEqual("##\n##\n", output)

    def test_display_width_height_x_y(self):
        s = Square(2, 1, 2)
        output = self.capture_from_stdout(s, "display").getvalue()
        self.assertEqual("\n\n ##\n ##\n", output)

    def test_display_changed_attribute(self):
        s = Square(2)
        s.size = 3
        output = self.capture_from_stdout(s, "display").getvalue()
        self.assertEqual("###\n###\n###\n", output)

    def test_display_one_arg(self):
        with self.assertRaises(TypeError):
            Square(99).display(3)

    def test_str_print_size(self):
        s = Square(2)
        actual = self.capture_from_stdout(s, "print").getvalue()
        expected = "[Square] ({}) 0/0 - 2\n".format(s.id)
        self.assertEqual(expected, actual)
    
    def test_str_size_x_y_id(self):
        s = Square(2, 6, 8, 10)
        self.assertEqual("[Square] (10) 6/8 - 2", str(s))

    def test_str_changed_attribute(self):
        s = Square(2, 6, 8, 10)
        s.size = 3
        self.assertEqual("[Square] (10) 6/8 - 3", str(s))

    def test_str_one_arg(self):
        with self.assertRaises(TypeError):
            Square(99, 99).__str__(99)

    def test_update_no_args(self):
        s = Square(2, 6, 8, 10)
        s.update()
        self.assertEqual("[Square] (10) 6/8 - 2", str(s))

    def test_update_four_args(self):
        s = Square(2, 6, 8, 10)
        s.update(12, 5, 7, 9)
        self.assertEqual("[Square] (12) 7/9 - 5", str(s))

    def test_update_more_than_four_args(self):
        s = Square(2, 6, 8, 10)
        s.update(12, 5, 9, 11, 7)
        self.assertEqual("[Square] (12) 9/11 - 5", str(s))

    def test_update_with_None(self):
        s = Square(2, 6, 8, 10)
        s.update(None)
        self.assertEqual("[Square] ({}) 6/8 - 2".format(s.id), str(s))

    def test_update_invalid_size_type(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(12, "invalid size")

    def test_update_size_zero(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(12, 0)

    def test_update_size_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(size=3)
        self.assertEqual("[Square] (10) 6/8 - 3", str(s))

    def test_update_four_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(size=3, id=5, x=7, y=9)
        self.assertEqual("[Square] (5) 7/9 - 3", str(s))

    def test_update_None_id_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(id=None)
        self.assertEqual("[Square] ({}) 6/8 - 2".format(s.id), str(s))

    def test_update_invalid_size_kwarg(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid size")

    def test_update_zero_size_kwarg(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_kwarg_skipped(self):
        s = Square(2, 6, 8, 10)
        s.update(3, 5, x=7)
        self.assertEqual("[Square] (3) 6/8 - 5", str(s))

    def test_update_wrong_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(q=7, w=9)
        self.assertEqual("[Square] (10) 6/8 - 2", str(s))

    def test_dictionary_one_arg(self):
        with self.assertRaises(TypeError):
            Square(3).to_dictionary(3)

    def test_to_dict_output(self):
        actual = Square(10, 1, 9, 1).to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'size': 10}
        self.assertEqual(actual, expected)

    def test_to_dict_changed_attribute(self):
        r1 = Square(10, 1, 9)
        r2 = Square(3, 5, 7)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())


if __name__ == "__main__":
    unittest.main()