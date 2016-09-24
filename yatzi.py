#!/usr/bin/python3

# Yatzi-terninger!

import random
from sys import stdin


class Dice:
    def __init(self):
        self.value = 1

    def roll(self):
        self.value = random.randint(1,6)

class Dices:

    def __init__(self, number):
        self.dices = [Dice() for i in range(number)]

    def roll(self, boolArray):
        for i in range(len(boolArray)):
            if not boolArray[i]:
                self.dices[i].roll()
        A = []
        for d in self.dices:
            A.append(d.value)
        print("Resultat: ", A)

    def length(self):
        return len(self.dices)

def firstRoll(dices):
    allFalse = [False] * 6
    inp = stdin.readline()
    dices.roll(allFalse)

def nextRoll(dices):
    while (True):
        inputList = []
        for x in stdin.readline().split():
            inputList.append(bool(int(x)))
        if (not len(inputList) == dices.length()):
            print("Vennligst skriv ", dices.length(), " tall")
            continue
        else:
            dices.roll(inputList)
            break

def main():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("**** MAXI YATZI ****\n\n")

    dices = Dices(6)

    # print("velg antall spillere:")
    # inp = stdin.readline()
    # x = int(inp)
    # for i in range(x):
        # print("Første spiller")

    print("Kast om hvem som starter")
    while(True):
        inputList = []
        for x in stdin.readline().split():
            inputList.append(x)
        if (len(inputList) >= 1):
            break
        firstRoll(dices)
        print("skriv noe når dere er klare")
    while (True):
        print("Klar for å kaste terningene?")

        firstRoll(dices)

        print("Velg hvilke terninger som taes vare på")

        nextRoll(dices)

        print("Siste kast! Velg hvilke terninger som taes vare på")

        nextRoll(dices)
        print("\nDet var det! Ny runde:")

if __name__ == "__main__":
    main()
