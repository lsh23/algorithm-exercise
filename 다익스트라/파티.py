from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, m: int, x: int, graph: [list[list[tuple[int, int]]]]) -> int:
        dists = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dist: list[int] = [100001] * (n + 1)
            dist[i] = 0
            q: deque[tuple[int, int]] = deque()
            q.append((0, i))
            while q:
                d, v = q.popleft()
                if dist[v] < d:
                    continue
                dist[v] = d
                for edge in graph[v]:
                    nxt_d, nxt = edge
                    q.append((d + nxt_d, nxt))
            dists[i] = dist

        ans: int = 0
        for i in range(1, n + 1):
            ans = max(dists[i][x] + dists[x][i], ans)
        return ans


if __name__ == "__main__":
    N: int
    M: int
    X: int
    graph = [list[list[tuple[int, int]]]]
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end, t = map(int, input().split())
        graph[start].append((t, end))
    print(Solution.solve(N, M, X, graph))
