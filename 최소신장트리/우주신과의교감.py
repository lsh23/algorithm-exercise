import math


def find(x: int, parent: list[int]) -> int:
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x], parent)
        return parent[x]


def merge(x: int, y: int, parent: list[int]):
    x = find(x, parent)
    y = find(y, parent)
    if x != y:
        parent[y] = x


def isUnion(x: int, y: int, parent: list[int]):
    x = find(x, parent)
    y = find(y, parent)
    return x == y


class Solution:
    @staticmethod
    def solve(n: int, m: int, points: list[list[int]], connected: list[list[int]]) -> float:

        edges: list[tuple[int, int, int]] = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                i_x, i_y = points[i]
                j_x, j_y = points[j]
                dist: float = math.sqrt((i_x - j_x) ** 2 + (i_y - j_y) ** 2)
                edges.append((dist, i, j))

        edges.sort()
        # print(edges)

        parent: list[int] = [i for i in range(n)]
        for c in connected:
            i, j = c
            merge(i, j, parent)
        # print(parent)

        ans: int = 0

        for edge in edges:
            dist, start, end = edge
            if isUnion(start, end, parent):
                continue
            merge(start, end, parent)
            ans += dist

        return round(ans, 2)


if __name__ == "__main__":
    N: int
    M: int
    points: list[list[int]]
    connected: list[list[int]]
    N, M = map(int, input().split())
    points = [[int(x) for x in input().split()] for _ in range(N)]
    connected = [[int(x) - 1 for x in input().split()] for _ in range(M)]
    print(f'{Solution.solve(N, M, points, connected):.2f}')
