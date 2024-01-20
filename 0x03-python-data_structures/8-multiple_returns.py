#!/usr/bin/python3

def multiple_returns(sentence):

    les_s = len(sentence)
    if les_s == 0:
        return ((0, None))
    else:
        return ((les_s, sentence[0]))
