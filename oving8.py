from sys import stdin


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


class MatrixKeeper:
    def __init__(self):
        self.matrix = []
        self.initialized = False
        self.startVal = 1

    def getMatrix(self, coins, value):
        if not self.initialized:
            self.initialized = True
            self.matrix = [[0 for _ in range(value + 1)] for _ in range(len(coins) + 1)]
            for i in range(value + 1):
                self.matrix[0][i] = i
            return self.matrix
        else:
            if value < len(self.matrix[0]):
                return self.matrix
            else:
                oldLength = len(self.matrix[0])
                diff_val = (value + 1 - oldLength)
                for row in self.matrix:
                    row.extend([0]*diff_val)
                for i in range(oldLength, value + 1):
                    self.matrix[0][i] = i
                self.startVal = oldLength
                return self.matrix

    def updateMatrix(self, matrix):
        self.matrix = matrix


def dynamic(coins, value, matrixKeeper):
    matrix = matrixKeeper.getMatrix(coins, value)
    startVal = matrixKeeper.startVal
    for c in range(1, len(coins) + 1):
        for val in range(startVal, value + 1):
            if coins[c - 1] == val:
                matrix[c][val] = 1
            elif coins[c - 1] > val:
                matrix[c][val] = matrix[c - 1][val]
            else:
                matrix[c][val] = min(matrix[c - 1][val], 1 + matrix[c][val - coins[c - 1]])
    matrixKeeper.updateMatrix(matrix)
    return matrix[-1][value]


def main():
    coins = []
    for c in stdin.readline().split():
        coins.append(int(c))
    coins.sort()

    # matrixKeeper = MatrixKeeper()
    # for line in stdin:
    #     print('value:', int(line))
    #     print('greedy-result:', incGreedy(coins, int(line)))
    #     print('\n -- running the dynamic algorithm -- ')
    #     print('dynamic-result:', dynamic(coins, int(line), matrixKeeper))
    #     print('')
    method = stdin.readline().strip()
    if method == "graadig" or (method == "velg" and isCanonical(coins)):
        for line in stdin:
            print(incGreedy(coins, int(line)))
    else:
        matrixKeeper = MatrixKeeper()
        for line in stdin:
            result = dynamic(coins, int(line), matrixKeeper)
            print(result)


if __name__ == "__main__":
    main()
