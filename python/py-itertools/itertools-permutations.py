# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

l=input().split()

a=list(permutations(list(l[0]),int(l[1])))
b=[]
for i in a:
    b.append(''.join(i))
b.sort()
for i in b:
    print(i)

