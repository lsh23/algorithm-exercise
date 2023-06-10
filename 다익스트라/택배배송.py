import heapq


class Solution:
    @staticmethod
    def solve(n: int, m: int, graph: list[list[tuple[int, int]]]) -> int:

        cost: list[int] = [1000000000] * (n + 1)

        cost[1] = 0

        pq: list[tuple[int, int]] = []

        for e in graph[1]:
            heapq.heappush(pq, e)

        while pq:
            c, nxt = heapq.heappop(pq)
            if c >= cost[nxt]:
                continue
            cost[nxt] = c
            for e in graph[nxt]:
                _c, _nxt = e
                heapq.heappush(pq, (c + _c, _nxt))

        return cost[n]


if __name__ == "__main__":
    N: int
    M: int
    graph: list[list[tuple[int, int]]]

    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        A_i, B_i, cost = map(int, input().split())
        graph[A_i].append((cost, B_i))
        graph[B_i].append((cost, A_i))

    print(Solution.solve(N, M, graph))
