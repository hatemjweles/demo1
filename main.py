import math
import os


def add(a, b) -> str:
    return math.floor(a + b)


def to_sentence(s) -> int:
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'




def fun():
    print("test")