##!/usr/bin/python3

import math
import random

charArray = []

i = 65
while (i<=90):
    charArray.append([chr(i)])
    i+=1

i = 97
while (i<=122):
    charArray.append([chr(i)])
    i+=1

i = 0
myChar = chr(65)
l = len(charArray)

while (i<1000000):
    charArray[random.randint(0,(l - 1))].append(i)

    if(random.randint(0,9) == 0):
        continue
    i+=1

for array in charArray:
    myString = array[0]
    myString += ':'
    k = 1
    while (k < len(array)):
        myString += str(array[k])
        myString += ','
        k+=1
    myString = myString[:-1]
    print(myString)
