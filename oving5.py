#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict

def alph(char):
    return (ord(char) - 97)

def countingSort(arr):
    counter = [0] * 26
    for a in arr:
        counter[alph(a)] += 1
    i = 0
    for i in range(26):
        counter[i] = counter[i] + counter[i - 1]

    i = 0
    [0] *
    for in range(len(arr), 0, -1):


    for a in range(27):
        for c in range(counter[a]):
            arr[i] = a
            i += 1
    return (arr,counter)

def countingsort( aList, k ):
    counter = [0] * ( k + 1 )
    for i in aList:
      counter[i] += 1

    ndx = 0;
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        aList[ndx] = i
        ndx += 1
        counter[i] -= 1

def insertionSort(A):
  for i in range(1, len(A)):
    tmp = A[i]
    k = i
    while k > 0 and tmp < A[k - 1]:
        A[k] = A[k - 1]
        k -= 1
    A[k] = tmp

def stringSort(start, end, arr, radix):


def flexradix(A, d):
    stringSort(0, (len(A) - 1), A, 1)

    return A

def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()
