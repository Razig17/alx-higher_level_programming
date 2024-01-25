#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) == str:
        for c in roman_string:
            if roman.get(c) <= num:
                num += roman.get(c)
            else:
                num = roman.get(c) - num
    return num
