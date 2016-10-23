from sys import stdin
from tabulate import tabulate


# incGreedy returns the minimum number of used coins found by the greedy algorithm
# where coins are sorted in increasing order
def incGreedy(coins, value):
    usedCoins = 0
    missedCoinsIndexes = []
    rem = value
    i = len(coins) - 1
    while (rem > 0):
        howMany = rem // coins[i]
        rem = rem % coins[i]
        if howMany == 0:
            missedCoinsIndexes.append(i)
        else:
            usedCoins += howMany
        i -= 1

    return usedCoins


def isTightCanonical(coins):  # coins sorted increasing
    last = len(coins) - 1
    nonGreedy = coins[last]//coins[last-1] + 1
    if (incGreedy(coins, nonGreedy*coins[last-1]) > nonGreedy):
        return False
    return True


def isCanonical(coins):  # coins sorted increasing
    for i in range(2, len(coins)):
        tightCoins = coins[:i+1]
        canonical = isTightCanonical(tightCoins)
        if not canonical:
            return False
    return True


def getMatrix(coins, value):
    matrix = [[0 for _ in range(value + 1)] for _ in range(len(coins) + 1)]
    for i in range(value + 1):
        matrix[0][i] = i
    return matrix


def dynamic(coins, value, matrix):
    for c in range(1, len(coins) + 1):
        for val in range(1, value + 1):
            if coins[c - 1] == val:
                matrix[c][val] = 1
            elif coins[c - 1] > val:
                matrix[c][val] = matrix[c - 1][val]
            else:
                matrix[c][val] = min(matrix[c - 1][val], 1 + matrix[c][val - coins[c - 1]])
    print(tabulate(matrix))
    return matrix[-1][-1]


def main():
    coins = []
    for c in stdin.readline().split():
        coins.append(int(c))
    coins.sort()
    # for line in stdin:
    #     print('value:', int(line))
    #     print('greedy-result:', incGreedy(coins, int(line)))
    #     matrix = getMatrix(coins, int(line))
    #     print('\n -- running the dynamic algorithm -- ')
    #     print('dynamic-result:', dynamic(coins, int(line), matrix))
    #     print('')
    method = stdin.readline().strip()
    if method == "graadig" or (method == "velg" and isCanonical(coins)):
        for line in stdin:
            print(incGreedy(coins, int(line)))
    else:
        for line in stdin:
            matrix = getMatrix(coins, int(line))
            result = dynamic(coins, int(line), matrix)
            print(result)


if __name__ == "__main__":
    main()
