#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict

def alph(char):
    return (ord(char) - 97)

def countingSort(start, end, A, r):
    counter = [0] * 26
    i = 0
    for i in range(start, (end + 1)):
        counter[alph(A[i][r])] += 1
    i = 0
    for i in range(26):
        counter[i] += counter[i - 1]

    B = [0] * (end - start + 1)
    i = 0
    for i in range(end, (start - 1), -1):
        print(A[i], 'r=', A[i][r], 'counter=', counter[alph(A[i][r])])
        B[counter[alph(A[i][r])] - 1] = A[i]
        counter[alph(A[i][r])] -= 1

    i = 0
    for i in range(end - start + 1):
        A[i + start] = B[i]

def stringSort(start, end, arr, radix):


def flexradix(A, d):
    stringSort(0, (len(A) - 1), A, 0)

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
