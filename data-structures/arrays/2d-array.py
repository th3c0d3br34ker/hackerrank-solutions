#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(A):
    smax = - 9 * 7
    for row in range(len(A) - 2):
        for column in range(len(A[row]) - 2):
            tl = A[row][column]
            tc = A[row][column + 1]
            tr = A[row][column + 2]
            mc = A[row + 1][column + 1]
            bl = A[row + 2][column]
            bc = A[row + 2][column + 1]
            br = A[row + 2][column + 2]
            s = tl + tc + tr + mc + bl + bc + br
            smax = max(s, smax)

    return(smax)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

