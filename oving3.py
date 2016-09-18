#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    deckLength = len(decks)
    print(decks)
    print (deckLength)
    deckIndexes = [0]*deckLength
    print (deckIndexes)
    index = 1
    mergedDecks = []
    #for i in range (deckLength) #vurder xrange
    print('DECKS:')
    for i in range(deckLength):
        print (decks[i])
    print('DECKS[i][k]')
    for i in range(deckLength):
        for k in range(len(decks[i])):
            print(i, ': ', decks[i][k])

    i = 0
    while (i<deckLength):
        if (deckIndexes[i] >= len(decks[i])):
            i += 1
            continue

        print('i:', end=' ')
        print(i, end=' deckIndexes[i]: ')
        print(deckIndexes[i], end=' deckNR: ')
        print(decks[i][deckIndexes[i]][0])

        if (decks[i][deckIndexes[i]][0] == index):
            mergedDecks.append(decks[i][deckIndexes[i]][1])
            print(decks[i][deckIndexes[i]][1])
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
