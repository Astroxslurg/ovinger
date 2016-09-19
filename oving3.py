#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    deckLength = len(decks)
    deckIndexes = [0]*deckLength
    index = 1
    mergedDecks = []
    numberOfCards = 0
    for k in decks:
        numberOfCards += len(k)

    i = 0
    while (index <= numberOfCards):
        if (i == deckLength):
            i = 0
            index += 1
            continue

        if (deckIndexes[i] >= len(decks[i])):
            i += 1
            continue

        if (decks[i][deckIndexes[i]][0] == index):
            mergedDecks.append(decks[i][deckIndexes[i]][1])
            index += 1
            deckIndexes[i] += 1
            i = 0
            continue

        i += 1

    returnString = ''.join(mergedDecks)
    return returnString

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
