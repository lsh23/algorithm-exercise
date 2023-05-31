import math
import heapq


class Solution:
    @staticmethod
    def solve(n: int, m: int, k: int, graph: list[list[int]], cities: list[int]) -> int:
        for i in range(1, n + 1):
            graph[i][i] = 0

        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        for g in graph:
            print(g)
        hq: list[int] = []
        for i in range(1, n + 1):
            max_dist = 0
            for city in cities:
                if city == i:
                    continue
                max_dist = max(max_dist, graph[city][i] + graph[i][city])
            heapq.heappush(hq, (max_dist, i))

        min_dist, x = heapq.heappop(hq)
        print(x, end=" ")
        while hq:
            dist, x = heapq.heappop(hq)
            if dist == min_dist:
                print(x, end=" ")


if __name__ == "__main__":
    N: int
    M: int
    graph: list[list[int]]
    K: int
    cities: list[int]
    N, M = map(int, input().split())
    graph = [[math.inf] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        A, B, T = map(int, input().split())
        graph[A][B] = T
    K = int(input())
    cities = [int(x) for x in input().split()]
    Solution.solve(N, M, K, graph, cities)
