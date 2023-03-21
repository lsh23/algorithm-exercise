class Solution:
    def solve(self, N:int, p1:int ,p2:int, graph: list[list[int]]):

        ans: int = -1
        visited: list[int] = [0] * (N+1)

        def dfs(cnt: int, p:int):
            nonlocal ans
            if p == p2:
                ans = cnt
                return
            for i in graph[p]:
                if visited[i] == 1:
                    continue
                visited[i] = 1
                dfs(cnt+1, i)
                visited[i] = 0

        visited[p1] = 1
        dfs(0, p1)

        return ans


if __name__ == "__main__":
    N: int
    M: int
    p1: int
    p2: int

    N = int(input())
    p1, p2 = map(int, input().split())
    M = int(input())

    graph: list[list[int]] = [ [] for _ in range(N+1) ]
    for _ in range(M):
        p, c = map(int, input().split())
        graph[p].append(c)
        graph[c].append(p)

    s: Solution = Solution()
    print(s.solve(N, p1, p2, graph))

