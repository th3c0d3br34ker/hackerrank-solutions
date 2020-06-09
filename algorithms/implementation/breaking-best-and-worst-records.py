#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_ctr=[scores[0],0]
    max_ctr=[scores[0],0]
    for i in scores:
        if(i<min_ctr[0]):
            min_ctr=[i,min_ctr[1]+1]
        if(i>max_ctr[0]):
            max_ctr=[i,max_ctr[1]+1]
    return [max_ctr[1],min_ctr[1]]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

