from sys import stdin
# from tabulate import tabulate
import heapq

Inf = float(1e3000)


def mst(nm):
    # print(tabulate(nm))
    maxWeight = 0
    h = []
    currentNodeNeighbours = nm[0]
    for i in range(1, len(currentNodeNeighbours)):
        heapq.heappush(h, (currentNodeNeighbours[i], (0, i - 1)))
    nm[0][0] = -1
    while h:
        # print(h)
        (weight, vertex) = heapq.heappop(h)
        # previous = vertex[0]
        nodeNum = vertex[1]
        # print(vertex, previous, nodeNum)
        # print(weight, vertex)
        while (nm[nodeNum][0] == -1):
            # print(h)
            # print('-- in while --', weight, vertex)
            if (weight == Inf) or (not h):
                return maxWeight
            (weight, vertex) = heapq.heappop(h)
            # previous = vertex[0]
            nodeNum = vertex[1]

        # print('chosenVertex: ', previous, '->', nodeNum, ':', weight)
        currentNodeNeighbours = nm[nodeNum]
        nm[nodeNum][0] = -1
        if weight > maxWeight:
            maxWeight = weight

        for i in range(1, len(currentNodeNeighbours)):
            heapq.heappush(h, (currentNodeNeighbours[i], (nodeNum, i - 1)))

    return maxWeight


def main():
    lines = []
    for str in stdin:
        lines.append(str)
    n = len(lines)
    neighbour_matrix = [None] * n
    node = 0
    for line in lines:
        neighbour_matrix[node] = [Inf] * (n + 1)
        for k in line.split():
            data = k.split(':')
            neighbour = int(data[0])
            weight = int(data[1])
            neighbour_matrix[node][neighbour + 1] = weight
        node += 1
    print(mst(neighbour_matrix))


if __name__ == "__main__":
    main()
