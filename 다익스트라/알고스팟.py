from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


class Solution:
    @staticmethod
    def solve(n: int, m: int, miro: list[list[int]]) -> int:
        ans: int = 10001
        q: deque[tuple[int, int, int]] = deque()
        visited: list[int] = [[0] * m for _ in range(n)]
        q.append((0, 0, 0))
        while q:
            y, x, cnt = q.popleft()
            if y == n - 1 and x == m - 1:
                ans = min(cnt, ans)
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny >= n or ny < 0 or nx >= m or nx < 0:
                    continue
                if visited[ny][nx] != 0:
                    continue

                visited[ny][nx] = 1

                if miro[ny][nx] == 1:
                    q.append((ny, nx, cnt + 1))
                else:
                    q.appendleft((ny, nx, cnt))

        return ans


if __name__ == "__main__":
    N: int
    M: int
    miro: list[list[int]]
    M, N = map(int, input().split())
    miro = [[int(x) for x in input()] for _ in range(N)]
    print(Solution.solve(N, M, miro))
