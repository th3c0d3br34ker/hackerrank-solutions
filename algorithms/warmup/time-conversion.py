#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    if(s[8:]=="AM"):
        if(s[0:2]=="12"):
            s="00"+s[2:8]
        else:
            s=s[:8]    
        return(s)
    if(s[8:]=="PM"):
        if(s[0:2]=="12"):
            s="12"+s[2:8]
        else:
            s=str(12+int(s[0:2]))+s[2:8]
        return(s)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

