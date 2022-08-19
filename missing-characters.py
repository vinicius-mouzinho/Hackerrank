import math
import os
import random
import re
import sys


def missingCharacters(s):
    abc = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    inputcharacs = list(s)
    for l in inputcharacs:
        if l in abc:
            abc.remove(l)
        if l in digits:
            digits.remove(l)
    outputdigits = ''.join(digits)
    outputabc = ''.join(abc)
    output = outputdigits + outputabc
    return output

         

if __name__ == '__main__':
    s = input()
    result = missingCharacters(s)
    print(result)

