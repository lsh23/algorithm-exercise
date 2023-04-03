from collections import deque


class Solution:
    @staticmethod
    def solve(r: int, c: int, river_info: list[list[str]]) -> int:
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        ans: int = 0
        visited: list[list[int]] = [[0] * c for _ in range(r)]

        water: deque[tuple[int, int]] = deque()
        swan: deque[tuple[int, int]] = deque()

        for i in range(r):
            for j in range(c):
                if river_info[i][j] != 'X':
                    water.append((i, j))
                if river_info[i][j] == 'L':
                    if len(swan) == 0:
                        visited[i][j] = 1
                        swan.append((i, j))

        while True:
            next_swan: deque[tuple[int, int]] = deque()
            while swan:
                y, x = swan.popleft()
                for i in range(4):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if next_y < 0 or next_y >= r or next_x < 0 or next_x >= c:
                        continue
                    if visited[next_y][next_x] != 0:
                        continue
                    visited[next_y][next_x] = 1
                    if river_info[next_y][next_x] == 'X':
                        next_swan.append((next_y, next_x))
                    if river_info[next_y][next_x] == '.':
                        swan.append((next_y, next_x))
                    if river_info[next_y][next_x] == 'L':
                        return ans

            swan = next_swan

            next_water: deque[tuple[int, int]] = deque()
            while water:
                y, x = water.popleft()
                for i in range(4):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if next_y < 0 or next_y >= r or next_x < 0 or next_x >= c:
                        continue
                    if river_info[next_y][next_x] == 'X':
                        river_info[next_y][next_x] = '.'
                        next_water.append((next_y, next_x))

            water = next_water

            ans += 1

        return ans


if __name__ == "__main__":
    R: int
    C: int
    river_info: list[list[str]]

    R, C = map(int, input().split())
    river_info = [[x for x in input()] for _ in range(R)]
    assert len(river_info) == R and len(river_info[0]) == C
    print(Solution.solve(R, C, river_info))
