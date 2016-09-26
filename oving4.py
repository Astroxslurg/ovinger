#!/usr/bin/python3

from sys import stdin
import math
# import time

class Bucket:
    elements = []
    def __init__(self):
        self.elements = []

sortedList = []

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

# def findFirstUp(B):
#     while
#
# def findFirstDown(B):
#     #
#
# def findUpper(B, upper, radix):
#     if (B.buckets):
#         z = math.floor((upper%(radix*10))/radix)
#         if (B.buckets[z].buckets or B.buckets[z].elements):
#             x = findUpper(B.buckets[z], upper, radix/10)
#             if (x >= 0):
#                 return x
#             if (x == -1):
#
#
#         while (not (B.buckets[z].buckets or B.buckets[z].elements)):
#             z += 1
#             if
#     else:
#         e = len(B.elements)
#         if (e == 1):
#             if (B.elements[e - 1] >= upper):
#                 return B.elements[e - 1]
#
#         else:
#             binarySearch(B.elements, upper, 0, e)

    # u = findUpper(B, upper, 100000)

def binarySearch(A, elem, s, e):
    if (s == (e - 1)):
        return s
    mid = math.floor((e - s)/2) + s
    # print('s: ', s, ' mid: ', mid, ' e: ', e)
    if (A[mid] == elem):
        return mid
    if (A[mid] > elem):
        return binarySearch(A, elem, s, mid)
    return binarySearch(A, elem, mid, e)

def find(A, lower, upper):
    e = len(A)
    if (e == 1):
        return [A[0],A[0]]
    u = binarySearch(A, upper, 0, e)
    if ((A[u] >= upper) or (u == (e - 1))):
        u = A[u]
    else:
        u = A[u + 1]

    l = binarySearch(A, lower, 0, e)
    if ((A[l] <= lower) or (l == 0)):
        l = A[l]
    else:
        l = A[l - 1]
    return [l,u]

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    # print(len(input_list), ' elements:')
    # startTime = time.time()
    sorted_list = sort_list(input_list)
    # print('superSort uses ', (time.time() - startTime), ' seconds')
    # print(sorted_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))
    # print('sort and search uses ', (time.time() - startTime), ' seconds')

if __name__ == "__main__":
    main()
