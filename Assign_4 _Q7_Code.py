import random
from math import gcd

# generate two random primes
p = random.randint(2, 999)
while True:
    q = random.randint(2, 999)
    if q != p:
        break

# calculate N and M
N = p * q
M = (p - 1) * (q - 1)

# find a random integer e such that gcd(e, M) = 1
while True:
    e = random.randint(3, M - 1)
    if gcd(e, M) == 1:
        break

# find a random integer x such that gcd(x, N) = 1
while True:
    x = random.randint(2, N - 1)
    if gcd(x, N) == 1:
        break

# generate the bit string x1x2...x100
bits = []
y = x
for i in range(100):
    y = pow(y, e, N)
    x = y % 2
    bits.append(str(x))

# print the results
print("p = ", p)
print("q = ", q)
print("e = ", e)
print("bits = ", "".join(bits))
