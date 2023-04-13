from itertools import combinations
from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, m: int, map_info: list[list[int]]) -> int:

        dy = [0, -1, 0, 1]
        dx = [1, 0, -1, 0]

        ans: int = 10000
        # 모든 빈칸에 바이러스가 있게 되는 최소 시간을 구해야함
        # 0 빈칸, 1 벽, 2 바이러스를 놓을 수 있는 칸
        # 바이러스는 1초에 상하좌우로 복제

        # 바이러스를 놓을 수 있는 칸
        virus_blocks: list[tuple[int, int]] = []
        empty_cnt: int = 0
        for i in range(n):
            for j in range(n):
                if map_info[i][j] == 2:
                    virus_blocks.append((i, j))
                if map_info[i][j] == 0:
                    empty_cnt += 1

        # 바이러스 M개를 활성화
        for virus in combinations(virus_blocks, m):
            tmp_map_info: list[list[int]] = [[x for x in y] for y in map_info]
            tmp_empty_cnt = empty_cnt
            dist: list[list[int]] = [[-1] * n for _ in range(n)]

            for v in virus:
                tmp_map_info[v[0]][v[1]] = -1  # 바이러스 활성화
                dist[v[0]][v[1]] = 0

            # 끝까지 퍼트리면서 시간을 잰다
            q: deque[tuple[int, int]] = deque(virus)
            while q:
                y, x = q.popleft()
                if tmp_empty_cnt == 0:
                    break
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue
                    if tmp_map_info[ny][nx] == 1:
                        continue
                    if dist[ny][nx] != -1:
                        continue
                    if tmp_map_info[ny][nx] == 0:
                        tmp_empty_cnt -= 1
                    dist[ny][nx] = dist[y][x] + 1
                    tmp_map_info[ny][nx] = -1
                    q.append((ny, nx))

            # print("map")
            # for tmi in tmp_map_info:
            #     print(tmi)
            #
            # print("dist")
            # for d in dist:
            #     print(d)

            # 모든 빈칸에 바이러스가 퍼졌는지 확인 후 최솟값 갱신
            if tmp_empty_cnt == 0:
                spread_time = 0
                for i in range(n):
                    for j in range(n):
                        spread_time = max(dist[i][j], spread_time)
                ans = min(spread_time, ans)

        if ans == 10000:
            return -1

        return ans


if __name__ == "__main__":
    N: int
    M: int
    map_info: list[list[int]]
    N, M = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, M, map_info))
