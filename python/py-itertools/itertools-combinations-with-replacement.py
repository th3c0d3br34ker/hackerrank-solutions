# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, i = input().split()
for i in combinations_with_replacement(sorted(s), int(i)):
    print("".join(i))

