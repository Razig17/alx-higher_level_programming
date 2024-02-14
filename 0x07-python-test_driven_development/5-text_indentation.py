#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of : [.] , [?] and [:]"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ch = " "
    ind = [".", "?", ":"]
    for i in range(len(text)):
        if ch[-1] == '\n' and text[i] == ' ':
            continue
        if text[i] in ind:
            ch += text[i] + "\n\n"
        else:
            ch += text[i]
    ch = ch.strip(" ")
    print(ch, end="")
