#!/usr/bin/python3

from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def buildTree(node, word, index=-1):
    index += 1
    if not word[index] in node.barn:
        node.barn[word[index]] = Node()

    if index == (len(word) - 1):
        return node.barn[word[index]]
    # else
    return buildTree(node.barn[word[index]], word, index)

def bygg(ordliste):
    toppNode = Node()
    for tuppel in ordliste:
        endNode = buildTree(toppNode, tuppel[0])
        endNode.posi.append(tuppel[1])
    return toppNode

def posisjoner(word, indeks, node):
    if indeks == len(word):
        return node.posi

    letter = word[indeks]
    indeks += 1
    if letter == '?':
        positions = []
        for key in node.barn:
            positions.extend(posisjoner(word, indeks, node.barn[key]))
        return positions
    elif letter in node.barn:
        return posisjoner(word, indeks, node.barn[letter])
    else:
        return []

def main():
    try:
        words = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in words:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()
