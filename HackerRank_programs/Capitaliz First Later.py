#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    # return " ".join([ss.capitalize() for ss in s.split(" ")])
    lis = s.split(" ")
    name = ""

    for word in lis:
        # print(":"+word+":")
        name = name + word.capitalize() + " "

    return name


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
