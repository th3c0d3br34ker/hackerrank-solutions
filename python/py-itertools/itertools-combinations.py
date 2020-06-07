# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s,k = input().split(' ')

for l in range(1,int(k)+1):
    for c in combinations (sorted(s),l):
        print(''.join(c))

