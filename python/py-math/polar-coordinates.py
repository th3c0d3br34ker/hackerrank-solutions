from math import sqrt
from cmath import phase
n = complex(input())

print(sqrt(pow(n.real, 2)+pow(n.imag, 2)))
print(phase(n))

