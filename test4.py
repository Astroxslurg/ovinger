#!/usr/bin/python3

# This script is intended for writing test-code for oving4.py

import random

maxInt = 999999
arrayLength = 100000
A = [''] * arrayLength

for i in range(arrayLength):
    num = random.randint(0, maxInt)
    A[i] = str(num)

print(' '.join(A))

querylength = 100
queryArr = [0,0]

for i in range(querylength):
    queryArr[0] = random.randint(0, maxInt)
    queryArr[1] = random.randint(0, maxInt)
    queryArr.sort()
    print(queryArr[0], queryArr[1])
