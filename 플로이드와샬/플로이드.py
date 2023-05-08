class Solution:
    @staticmethod
    def solve(n:int, m:int, graph:list[list[int]]) -> None:
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][j] >= graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]

        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1000_000_000:
                    graph[i][j] = 0
                print(graph[i][j], end=" ")
            print()


if __name__ == "__main__":
    n: int
    m: int
    graph: list[list[int]]
    n = int(input())
    m = int(input())
    graph = [[1000_000_000]*n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for _ in range(m):
        a,b,c = map(int, input().split())
        graph[a-1][b-1] = c if graph[a-1][b-1] > c else graph[a-1][b-1]
    Solution.solve(n,m,graph)