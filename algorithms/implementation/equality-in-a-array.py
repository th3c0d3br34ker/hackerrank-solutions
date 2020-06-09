#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
   
def equalizeArray(arr):
    max_occur=[0,0]
    for i in arr:
        t = arr.count(i)
        if(t>max_occur[1]):
            max_occur=[i,t]
    return len(remove_values_from_list(arr,max_occur[0]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

