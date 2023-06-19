from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


class Solution:
    @staticmethod
    def solve(n: int, m: int, map_info: list[list[int]]):
        start: tuple[int, int]
        for i in range(n):
            for j in range(m):
                if map_info[i][j] == 2:
                    start = (i, j)

        q: deque[tuple[int, int, int]] = deque()
        dist: list[list[int]] = [[0] * m for _ in range(n)]

        q.append((start[0], start[1], 0))
        while q:
            y, x, d = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if map_info[ny][nx] != 1:
                    continue
                if dist[ny][nx] != 0:
                    continue
                dist[ny][nx] = d + 1
                q.append((ny, nx, d + 1))

        for i in range(n):
            for j in range(m):
                if map_info[i][j] == 1 and dist[i][j] == 0:
                    dist[i][j] = -1

        for d in dist:
            print(*d, sep=" ")


if __name__ == "__main__":
    N: int
    M: int
    map_info: list[list[int]]
    N, M = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(N)]
    Solution.solve(N, M, map_info)
