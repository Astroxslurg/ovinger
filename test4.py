#!/usr/bin/python3

# This script is intended for writing test-code for oving4.py

import random

maxInt = 999999
arrayLength = 10000
A = [''] * arrayLength

for i in range(arrayLength):
    num = random.randint(0, maxInt)
    A[i] = str(num)

print(' '.join(A))
