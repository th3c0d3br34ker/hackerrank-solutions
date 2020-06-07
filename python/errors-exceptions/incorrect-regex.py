# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for _ in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print('False')

