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


def best_path(nm, prob):
    print('prob:', prob)
    h = MaxHeap()
    h.insert(1, 0)
    totProb = [0]*len(prob)
    totProb[0] = prob[0]
    pi = [-1]*len(prob)
    p = len(pi) - 1
    while(1 < len(h.list)):
        node = h.pop()[1]
        if node == p:
            break
        for i, n in enumerate(nm[node]):
            if n:
                tp = totProb[node]*prob[i]
                print(node, '->', i, 'tp:', tp)
                if (tp > totProb[i]):
                    totProb[i] = tp
                    h.insert(prob[i], i)
                    pi[i] = node
        print('totProb:', totProb)
        print('pi:', pi)
        print('h:', h.list)

    path = [str(p)]
    while True:
        p = pi[p]
        if p == -1:
            break
        path.append(str(p))
    path.reverse()
    print(path)
    spath = "-".join(path)
    return spath


def main():
    n = int(stdin.readline())
    probabilities = [float(x) for x in stdin.readline().split()]
    neighbour_matrix = []
    for line in stdin:
        neighbour_row = [0] * n
        neighbours = [int(neighbour) for neighbour in line.split()]
        for neighbour in neighbours:
            neighbour_row[neighbour] = 1
        neighbour_matrix.append(neighbour_row)
    print(best_path(neighbour_matrix, probabilities))


if __name__ == "__main__":
    main()
