from itertools import combinations
from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, m: int, map_info: list[list[int]]) -> int:

        ans: int = 0

        dy = [0, -1, 0, 1]
        dx = [1, 0, -1, 0]
        blank: list[tuple[int, int]] = []
        virus: list[tuple[int, int]] = []
        for i in range(n):
            for j in range(m):
                if map_info[i][j] == 0:
                    blank.append((i, j))
                if map_info[i][j] == 2:
                    virus.append((i, j))

        # 벽 3개 새로 세우기 -> 24C3
        for new_walls in combinations(blank, 3):
            tmp_map_info: list[list[int]] = [[x for x in y] for y in map_info]

            for new_wall in new_walls:
                tmp_map_info[new_wall[0]][new_wall[1]] = 1

            # 바이러스 퍼트리기 -> N*M
            visited: list[list[int]] = [[0] * m for _ in range(n)]
            q: deque[tuple[int, int]] = deque()

            for v in virus:
                v_y, v_x = v
                visited[v_y][v_x] = 1
                q.append(v)

            while q:
                y, x = q.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        continue
                    if tmp_map_info[ny][nx] == 1:
                        continue
                    if visited[ny][nx] != 0:
                        continue
                    visited[ny][nx] = 1
                    tmp_map_info[ny][nx] = 2
                    q.append((ny, nx))

            # print("-----")
            # for w in tmp_map_info:
            #     print(w)
            # 안전 영역 크기 최댓값 갱신
            safe_zone_size: int = 0
            for i in range(n):
                for j in range(m):
                    if tmp_map_info[i][j] == 0:
                        safe_zone_size += 1

            ans = max(safe_zone_size, ans)
        return ans


if __name__ == "__main__":
    N: int
    M: int
    map_info: list[list[int]]

    N, M = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(N)]
    assert len(map_info) == N and len(map_info[0]) == M

    print(Solution.solve(N, M, map_info))
