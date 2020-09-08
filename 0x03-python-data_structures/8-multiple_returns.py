#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    first_char = sentence[0]
    if a > 0:
        return (a, first_char)
    else:
        return (0, None)
