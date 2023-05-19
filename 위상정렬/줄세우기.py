from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, m: int, graph: list[list[int]], indegree: list[int]) -> int:
        visited: list[int] = [0] * (n + 1)
        q: deque[int] = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0 and visited[i] == 0:
                visited[i] = 1
                q.append(i)

        while q:
            x = q.popleft()
            print(x, end=" ")
            for next in graph[x]:
                indegree[next] -= 1
                if indegree[next] == 0 and visited[next] == 0:
                    visited[next] = 1
                    q.append(next)


if __name__ == "__main__":
    N: int
    M: int
    graph: list[list[int]]
    indegree: list[int]
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        indegree[B] += 1

    Solution.solve(N, M, graph, indegree)
