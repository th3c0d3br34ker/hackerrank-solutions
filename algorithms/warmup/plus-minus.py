#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    neg=0
    pos=0
    zero=0
    for i in range(len(arr)):
        if(arr[i]==0):
            zero+=1
        if(arr[i]>0):
            pos+=1
        if(arr[i]<0):
            neg+=1
    print("{:.6f}".format(pos/len(arr)))
    print("{:.6f}".format(neg/len(arr)))    
    print("{:.6f}".format(zero/len(arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

