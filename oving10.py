from sys import stdin
import heapq

Inf = float(1e3000)


def mst(nm):
    maxWeight = 0
    h = []
    currentNodeNeighbours = nm[0]
    for i in range(1, len(currentNodeNeighbours)):
        if not (currentNodeNeighbours[i] == Inf):
            heapq.heappush(h, (currentNodeNeighbours[i], i - 1))
    nm[0][0] = -1
    while h:
        (weight, nodeNum) = heapq.heappop(h)
        while (nm[nodeNum][0] == -1):
            if (not h):
                return maxWeight
            (weight, nodeNum) = heapq.heappop(h)

        currentNodeNeighbours = nm[nodeNum]
        nm[nodeNum][0] = -1
        if weight > maxWeight:
            maxWeight = weight

        for i in range(1, len(currentNodeNeighbours)):
            if not (currentNodeNeighbours[i] == Inf):
                heapq.heappush(h, (currentNodeNeighbours[i], i - 1))

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
