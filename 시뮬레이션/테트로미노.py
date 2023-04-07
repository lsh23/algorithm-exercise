class Solution:
    @staticmethod
    def solve(n: int, m: int, paper: list[list[int]]) -> int:
        ans: int = 0

        dy = [0, -1, 0, 1]
        dx = [1, 0, -1, 0]

        visited: list[list[int]] = [[0] * m for _ in range(n)]

        def dfs(y: int, x: int, sum: int, L: int):
            nonlocal ans
            if L == 4:
                ans = max(sum, ans)
                return
            for i in range(4):
                next_y = y + dy[i]
                next_x = x + dx[i]
                if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                    continue
                if visited[next_y][next_x] != 0:
                    continue
                visited[next_y][next_x] = 1
                dfs(next_y, next_x, sum + paper[next_y][next_x], L + 1)
                visited[next_y][next_x] = 0

        for i in range(n):
            for j in range(m):
                visited[i][j] = 1
                dfs(i, j, paper[i][j], 1)
                visited[i][j] = 0
                # ㅜ
                if j + 2 < m and i + 1 < n:
                    ans = max(ans, paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j + 1])
                # ㅏ
                if j + 1 < m and i + 2 < n:
                    ans = max(ans, paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 1][j + 1])
                # ㅗ
                if j + 2 < m and i - 1 >= 0:
                    ans = max(ans, paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i - 1][j + 1])
                # ㅓ
                if j - 1 >= 0 and i + 2 < n:
                    ans = max(ans, paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 1][j - 1])

        return ans


if __name__ == "__main__":
    N: int
    M: int
    paper: list[list[int]]
    N, M = map(int, input().split())
    paper = [[int(x) for x in input().split()] for _ in range(N)]
    assert len(paper) == N and len(paper[0]) == M
    print(Solution.solve(N, M, paper))
