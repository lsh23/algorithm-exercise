class Solution:
    @staticmethod
    def solve(n: int, m: int, graph: list[list[int]], plan: list[int]):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if graph[i][j] == 0:
                    graph[i][j] = 201

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]

        for g in graph:
            print(g)

        for i in range(m - 1):
            if graph[plan[i]][plan[i + 1]] == 201:
                return "NO"

        return "YES"


if __name__ == "__main__":
    N: int
    M: int
    graph: list[list[int]]
    plan: list[int]
    N = int(input())
    M = int(input())
    graph = [[int(x) for x in input().split()] for _ in range(N)]
    plan = [int(x) - 1 for x in input().split()]
    print(Solution.solve(N, M, graph, plan))
