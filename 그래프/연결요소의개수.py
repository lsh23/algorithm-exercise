class Solution:
    def solve(self, N:int, graph:list[list[int]]):

        def DFS(k:int):
            for j in graph[k]:
                if visited[j] == 0:
                    visited[j] = 1
                    DFS(j)

        cnt: int = 0
        visited: list[int] = [0]*(N+1)
        for i in range(1, N+1):
            if visited[i] == 0:
                visited[i] = 1
                DFS(i)
                cnt += 1
        return cnt


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)

    N: int
    M: int
    N, M = map(int, input().split())
    graph: list[list[int]] = [ [] for _ in range(N+1)]
    for _ in range(M):
        u: int
        v: int
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    s: Solution = Solution()
    print(s.solve(N,graph))
