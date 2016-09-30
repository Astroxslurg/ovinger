#!/usr/bin/python3

#Euclidean Algorithm
from sys import stdin
import fractions
import random

def gcd(a, b):
    n = max(a, b)
    k = min(a, b)
    r = n%k
    print(n, ' = ', k, '*', n//k, ' + ', r, sep='')
    while (not r == 0):
        n = k
        k = r
        r = n%k
        print(n, ' = ', k, '*', n//k, ' + ', r, sep='')

    return k

def main():
    # length = 1000000
    # for i in range(length):
        # x = random.randint(1,1000)
        # y = random.randint(1,1000)
        # while (x == y):
            # y = random.randint(1,1000)
        # if (not (gcd(x,y) == fractions.gcd(x,y))):
            # print('euclid:', gcd(x,y))
            # print('fractions:', fractions.gcd(x,y))

    for line in stdin:
        word = line.split()
        a = int(word[0])
        b = int(word[1])
        print("")
        print(gcd(a, b))

if __name__ == "__main__":
    main()
