from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


class Solution:
    @staticmethod
    def solve(r: int, c: int, map_info: list[list[int]]) -> None:

        hours: int = 0

        while True:
            removed: list[tuple[int, int]] = []
            q: deque[tuple[int, int]] = deque()
            visited: list[list[int]] = [[0] * c for _ in range(r)]
            visited[0][0] = 1
            q.append((0, 0))
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if ny < 0 or ny >= r or nx < 0 or nx >= c:
                        continue
                    if visited[ny][nx] != 0:
                        continue
                    if map_info[ny][nx] == 1:
                        removed.append((ny, nx))
                        visited[ny][nx] = 1
                        continue
                    visited[ny][nx] = 1
                    q.append((ny, nx))

            removed_cnt: int = len(removed)
            for cheese in removed:
                y, x = cheese
                map_info[y][x] = 0

            hours += 1

            if sum([sum(row) for row in map_info]) == 0:
                print(hours)
                print(removed_cnt)
                break


if __name__ == "__main__":
    R: int
    C: int
    map_info: list[list[int]]
    R, C = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(R)]
    Solution.solve(R, C, map_info)
