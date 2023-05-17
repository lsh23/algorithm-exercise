import math
import heapq


class Solution:
    @staticmethod
    def solve(v: int, e: int, k: int, graph: list[list[int]]) -> None:
        pq: list[tuple[int, int]] = []
        dist: list[int] = [math.inf] * v
        dist[k] = 0
        heapq.heappush(pq, (dist[k], k))

        while pq:
            _dist, _start = heapq.heappop(pq)

            if dist[_start] < _dist:
                continue

            for edge in graph[_start]:
                _end, _cost = edge
                if dist[_start] + _cost < dist[_end]:
                    dist[_end] = dist[_start] + _cost
                    heapq.heappush(pq, (dist[_end], _end))

        for d in dist:
            if d == math.inf:
                print("INF")
            else:
                print(d)


if __name__ == "__main__":
    V: int
    E: int
    K: int
    graph: list[list[tuple[int, int]]]
    V, E = map(int, input().split())
    K = int(input())
    graph = [[] * V for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u - 1].append((v - 1, w))
    Solution.solve(V, E, K-1, graph)
