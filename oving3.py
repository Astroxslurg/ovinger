#!/usr/bin/python3

from sys import stdin
from itertools import repeat

import math
import sys

def mergeTwo(deck1, deck2):
    length = len(deck1) + len(deck2)
    i1 = 0
    i2 = 0
    deck1.append(((sys.maxsize), 'X'))
    deck2.append(((sys.maxsize), 'X'))
    mergedDeck = [[] for i in range(length)]
    for k in range(0, length):
        if (deck1[i1][0] < deck2[i2][0]):
            mergedDeck[k] = deck1[i1]
            i1 += 1
        else:
            mergedDeck[k] = deck2[i2]
            i2 += 1
    return mergedDeck

def merge(decks):
    deckLength = len(decks)

    while (deckLength > 1):
        i = 1
        while (i < deckLength):
            decks[math.floor(i/2)] = mergeTwo(decks[i-1], decks[i])
            i += 2
        if (i == deckLength):
            decks[math.floor(i/2)] = decks[i-1]
        deckLength = math.ceil(deckLength/2)

    totalLength = len(decks[0])
    letterArray = [chr(97)]*totalLength
    k = 0
    while (k < totalLength):
        letterArray[k] = decks[0][k][1]
        k += 1

    return ''.join(letterArray)

def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))

if __name__ == "__main__":
    main()
