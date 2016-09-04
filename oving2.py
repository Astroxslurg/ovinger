#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def printTree(node, thisKey):
    print(thisKey, end=' ')
    print(node.posi)
    for key in node.barn:
        printTree(node.barn[key], key)

def buildTree(node, word):
    letter = word[0]
    print(letter, end=' ')
    print(node.posi)
    word = word[1:]
    if not letter in node.barn:
        node.barn[letter] = Node()

    if not word:
        return node.barn[letter]
    #else
    return buildTree(node.barn[letter], word)

def bygg(ordliste):
    toppNode = Node()
    for tuppel in ordliste:
        endNode = buildTree(toppNode, tuppel[0])
        endNode.posi.append(tuppel[1])
    printTree(toppNode, 'toppNode')
    return toppNode

def posisjoner(ord, indeks, node):
    y = [1] * 5
    return y

def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
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
