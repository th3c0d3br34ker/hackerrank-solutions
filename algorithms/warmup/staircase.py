#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    t=""
    for i in range(n):
        t=""
        for j in range(n-i-1):
            t=t+" "
        print(t,end="")
        t=""
        for j in range(i+1):
            t=t+"#"
        print(t)

if __name__ == '__main__':
    n = int(input())

    staircase(n)

