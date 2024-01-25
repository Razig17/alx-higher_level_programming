#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    subtract = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) == str:
        pre = roman_string[0]
        for c in roman_string:

            if pre + c in subtract.keys():
                
                num += subtract.get(pre + c) - roman.get(pre)
            else:
                num = roman.get(c) + num
            pre = c

    return num
