#!/usr/bin/python3
"""Unittests module for max_integer([]) function"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for testing max_integer([]) function"""

    def test_integers(self):
        """ Test integers"""
        self.assertEqual(max_integer([55, 66, 77, 88]), 88)

    def test_one_integer(self):
        """Test one integer"""
        self.assertEqual(max_integer([-800]), -800)

    def test_ints_floats(self):
        """ Test integers and floats"""
        self.assertEqual(max_integer([11, 22.5, 22, 11.5]), 22.5)
        self.assertEqual(max_integer([33, 33.0, 33.2, -33]), 33.2)

    def test_string(self):
        """Test a string"""
        self.assertEqual(max_integer("alx"), "x")

    def test_tuples(self):
        """ Test a tuple"""
        self.assertEqual(max_integer((99, 88)), 99)

    def test_list_of_strings(self):
        """ Test a list of strings"""
        self.assertEqual(max_integer(["a", "l", "x"]), "x")
        self.assertEqual(max_integer(["alx", "axx"]), "axx")

    def test_empty(self):
        """ Test an empty list"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)
