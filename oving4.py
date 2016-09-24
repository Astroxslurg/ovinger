#!/usr/bin/python3

from sys import stdin
import math
import time

class Bucket:
    elements = []
    def __init__(self):
        self.elements = []

sortedList = []

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def insertionSort(A):
  for i in range(1, len(A)):
    tmp = A[i]
    k = i
    while k > 0 and tmp < A[k - 1]:
        A[k] = A[k - 1]
        k -= 1
    A[k] = tmp

def bucketSort(bucket, radix):
    if ((radix == 1) or (len(bucket.elements) < 16)):
        insertionSort(bucket.elements)
        sortedList.extend(bucket.elements)
        # print('sorted: ', bucket.elements)
    else:
        bucket.buckets = [Bucket() for i in range(10)]
        for element in bucket.elements:
            z = math.floor((element%(radix*10))/radix)
            bucket.buckets[z].elements.append(element)
        for b in bucket.buckets:
            if (b.elements):
                bucketSort(b, radix/10)

def sort_list(A):
    topBucket = Bucket()
    topBucket.elements = A
    bucketSort(topBucket, 100000)

    return sortedList


def find(A, lower, upper):

    return [0,0]


def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    print('10 000 elements:')
    startTime = time.time()
    sorted_list = insertionSort(input_list)
    print('mergeSort uses ', (time.time() - startTime), ' seconds')
    startTime = time.time()
    sorted_list = sort_list(input_list)
    print('superSort uses ', (time.time() - startTime), ' seconds')
    startTime = time.time()
    sorted_list = input_list.sort()
    print('insertionSort uses ', (time.time() - startTime), ' seconds')
    startTime = time.time()
    sorted_list = mergeSort(input_list)
    print('timSort uses ', (time.time() - startTime), ' seconds')
    # print(sorted_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
