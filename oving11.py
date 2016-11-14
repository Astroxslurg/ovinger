from sys import stdin


# MaxHeap is missing buildHeap, because it is not needed in this script
class MaxHeap:
    def __init__(self):
        self.list = [0]
        self.size = 0

    def bubbleUp(self, index):
        while (index // 2) > 0:
            if self.list[index][0] > self.list[index // 2][0]:
                tmp = self.list[index // 2]
                self.list[index // 2] = self.list[index]
                self.list[index] = tmp
            index = index // 2

    def insert(self, prob, node):
        self.list.append((prob, node))
        self.size = self.size + 1
        self.bubbleUp(self.size)

    def minChild(self, index):
        if ((index * 2) + 1) > self.size:
            return index * 2
        else:
            if self.list[index*2][0] > self.list[index*2+1][0]:
                return index * 2
            else:
                return index * 2 + 1

    def sinkDown(self, index):
        while (index * 2) <= self.size:
            mc = self.minChild(index)
            if self.list[index][0] < self.list[mc][0]:
                tmp = self.list[index]
                self.list[index] = self.list[mc]
                self.list[mc] = tmp
            index = mc

    def pop(self):
        if self.size == 0:
            return -1
        retval = self.list[1]
        self.list[1] = self.list[self.size]
        self.size = self.size - 1
        self.list.pop()
        self.sinkDown(1)
        return retval

    def list(self):
        return self.list


def best_path(nl, prob):
    h = MaxHeap()
    heapInsert = h.insert
    heapPop = h.pop
    heapList = h.list
    heapInsert(prob[0], 0)
    totProb = [0]*len(prob)
    totProb[0] = prob[0]
    pi = [-1]*len(prob)
    p = len(pi) - 1
    while(1 < len(heapList)):
        node = heapPop()[1]
        if node == p:
            break
        for n in nl[node]:
            tp = totProb[node]*prob[n]
            if (tp > totProb[n]):
                totProb[n] = tp
                heapInsert(tp, n)
                pi[n] = node

    path = [str(p)]
    pathAppend = path.append
    while True:
        p = pi[p]
        if p == -1:
            break
        pathAppend(str(p))
    if (len(path) == 1):
        return 0
    path.reverse()
    spath = "-".join(path)
    return spath


def main():
    n = int(stdin.readline())
    probabilities = [float(x) for x in stdin.readline().split()]
    neighbourLists = [[] for i in range(n)]
    i = 0
    for line in stdin:
        neighbourLists[i] = [int(neighbour) for neighbour in line.split()]
        i = i + 1
    print(best_path(neighbourLists, probabilities))


if __name__ == "__main__":
    main()
