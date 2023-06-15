from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


class Solution:
    @staticmethod
    def solve(n: int, map_info: list[list[int]]):
        q: deque[tuple[int, int, int]] = deque()
        total_lost: list[list[int]] = [[9 * 125] * n for _ in range(n)]
        total_lost[0][0] = map_info[0][0]
        q.append((0, 0))
        while q:
            y, x = q.popleft()
            if y == n - 1 and x == n - 1:
                continue
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if total_lost[ny][nx] > total_lost[y][x] + map_info[ny][nx]:
                    total_lost[ny][nx] = total_lost[y][x] + map_info[ny][nx]
                    q.append((ny, nx))
        return total_lost[n - 1][n - 1]


if __name__ == "__main__":
    i: int = 1
    while True:
        N: int = int(input())
        if N == 0:
            break
        map_info: list[list[int]] = [[int(x) for x in input().split()] for _ in range(N)]
        print(f'Problem {i}: {Solution.solve(N, map_info)}')
        i += 1
