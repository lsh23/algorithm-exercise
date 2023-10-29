import heapq


def find(x: int, parent: list[int]) -> int:
    if x == parent[x]:
        return x
    parent[x] = find(parent[x], parent)
    return parent[x]


def merge(x: int, y: int, parent: list[int]):
    x = find(x, parent)
    y = find(y, parent)
    parent[y] = x


def isUnion(x: int, y: int, parent: list[int]) -> bool:
    return find(x, parent) == find(y, parent)


class Solution:
    @staticmethod
    def solve(n: int, w_i: list[int], p_ij: list[list[int]]) -> int:
        p_ij.append(w_i)
        q: list[tuple[int, int]] = []
        for i in range(n + 1):
            for j in range(n):
                q.append((p_ij[i][j], i, j))

        heapq.heapify(q)
        parent: list[int] = [x for x in range(n + 1)]
        link_cost: int = 0
        while q:
            cost, i, j = heapq.heappop(q)
            if isUnion(i, j, parent):
                continue
            merge(i, j, parent)
            link_cost += cost

        return link_cost


if __name__ == "__main__":
    N: int
    W_i: list[int]
    P_ij: list[list[int]]
    N = int(input())
    W_i = [int(input()) for _ in range(N)]
    P_ij = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, W_i, P_ij))
