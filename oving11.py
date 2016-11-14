from sys import stdin


# maxHeap is missing buildHeap, because it is not needed in this script
class maxHeap:
    def __init__(self):
        self.list = [0]
        self.size = 0

    def bubbleUp(self, index):
        while (index // 2) > 0:
            if self.list[index] > self.list[index // 2]:
                tmp = self.list[index // 2]
                self.list[index // 2] = self.list[index]
                self.list[index] = tmp
            index = index // 2

    def insert(self, item):
        self.list.append(item)
        self.size = self.size + 1
        self.bubbleUp(self.size)

    def minChild(self, index):
        if ((index * 2) + 1) > self.size:
            return index * 2
        else:
            if self.list[index*2] > self.list[index*2+1]:
                return index * 2
            else:
                return index * 2 + 1

    def sinkDown(self, index):
        while (index * 2) <= self.size:
            mc = self.minChild(index)
            if self.list[index] > self.list[mc]:
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


def best_path(nm, prob):
    print('prob', prob)
    q = deque([0])
    totProb = [0]*len(prob)
    totProb[0] = prob[0]
    pi = [-1]*len(prob)
    while(q):
        node = q.pop()
        for i, n in enumerate(nm[node]):
            if n:
                tp = totProb[node]*prob[i]
                print(node, '->', i, 'tp:', tp)
                if (tp > totProb[i]):
                    totProb[i] = tp
                    q.appendleft(i)
                    pi[i] = node
        print('totProb:', totProb)
        print('pi:', pi)
        print('q:', q)

    p = len(pi) - 1
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
