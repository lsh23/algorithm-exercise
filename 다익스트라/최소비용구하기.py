import math
import heapq


class Solution:
    @staticmethod
    def solve(n: int, graph: int, start: int, end: int) -> int:
        pq: list[tuple[int, int]] = []
        dist: list[int] = [math.inf] * n
        dist[start] = 0
        heapq.heappush(pq, (dist[start], start))

        while pq:
            _dist, _start = heapq.heappop(pq)

            if dist[_start] < _dist:
                continue

            for edge in graph[_start]:
                _end, _cost = edge
                if dist[_start] + _cost < dist[_end]:
                    dist[_end] = dist[_start] + _cost
                    heapq.heappush(pq, (dist[_end], _end))

        return dist[end]


if __name__ == "__main__":
    N: int
    M: int
    graph: list[list[tuple[int, int]]]
    start: int
    end: int
    N = int(input())
    M = int(input())
    graph = [[] * N for _ in range(N)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[s - 1].append((e - 1, c))
    start, end = map(int, input().split())
    print(Solution.solve(N, graph, start - 1, end - 1))
