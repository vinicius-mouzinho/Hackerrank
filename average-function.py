# Create a function to determine the average of a number with 2 floating points.

import math
import os
import random
import re
import sys


def avg(*int):
    numbers = [int]
    sum = 0
    div = 0
    for num in int:
        sum += num
        div += 1
    return sum / div


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    res = avg(*nums)
    print(f'{float(res):.2f}')