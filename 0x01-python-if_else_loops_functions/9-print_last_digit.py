#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of a number."""
    last = abs(number) % 10
    print(last, end="")
    return(last)
