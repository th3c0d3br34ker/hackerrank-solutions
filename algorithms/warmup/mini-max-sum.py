#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minarr=arr.copy()
    minarr.sort(key=None)
    maxarr=arr.copy()
    maxarr.sort(key=None,reverse=True)
    l=[]
    l.append(sum(minarr[:-1]))
    l.append(sum(maxarr[:-1]))
    print("{} {}".format(l[0],l[1]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

