class Solution:
    @staticmethod
    def solve(n: int, m: int, r: int, items: list[int], graph: list[list[int]]) -> int:
        for i in range(n):
            graph[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        ans: int = 0

        for i in range(n):
            sum: int = 0
            for j in range(n):
                if graph[i][j] <= m:
                    sum += items[j]
            ans = max(sum, ans)

        return ans


if __name__ == "__main__":
    n: int
    m: int
    r: int
    items: list[int]
    graph: list[list[int]]
    n, m, r = map(int, input().split())
    items = [int(x) for x in input().split()]
    graph = [[100000000] * n for _ in range(n)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a - 1][b - 1] = l
        graph[b - 1][a - 1] = l
    print(Solution.solve(n, m, r, items, graph))
