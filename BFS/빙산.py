from collections import deque


class Solution:
    def solve(self, n: int, m: int, icebergs_info: list[list[int]]) -> int:

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        after_year: int = 0

        q: deque[tuple[int, int]] = deque()
        while True:
            # 현재 섬의 갯수를 센다
            iceberg_island_cnt: int = 0
            visited: list[list[int]] = [[0] * m for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    # 빙하섬의 갯수가 2개 이상이면 정답 리턴
                    if iceberg_island_cnt == 2:
                        # print(f'iceberg_island_cnt {iceberg_island_cnt}')
                        # for x in visited:
                        #     print(x)
                        return after_year
                    if icebergs_info[i][j] != 0 and visited[i][j] == 0:
                        iceberg_island_cnt += 1
                        visited[i][j] = 1
                        q.append((i, j))
                        while q:
                            y, x = q.popleft()
                            for k in range(4):
                                next_y = y + dy[k]
                                next_x = x + dx[k]
                                if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                                    continue
                                if visited[next_y][next_x] == 1:
                                    continue
                                if icebergs_info[next_y][next_x] == 0:
                                    continue
                                visited[next_y][next_x] = 1
                                q.append((next_y, next_x))

            # print(f'iceberg_island_cnt {iceberg_island_cnt}')
            # for x in visited:
            #     print(x)

            # 현재 빙하 위치
            for i in range(n):
                for j in range(m):
                    if icebergs_info[i][j] != 0:
                        q.append((i, j))
            if not q:
                break

            # bfs 하면서 1년 후의 녹은 후의 모습 구한다
            after_year += 1
            after_icebergs_info = [[0] * m for _ in range(n)]
            while q:
                y, x = q.popleft()
                after_icebergs_info[y][x] = icebergs_info[y][x]
                for i in range(4):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                        continue
                    if after_icebergs_info[y][x] == 0:
                        continue
                    if icebergs_info[next_y][next_x] == 0:
                        after_icebergs_info[y][x] -= 1

            # print(f'after {after_year}')
            # for x in after_icebergs_info:
            #     print(x)

            icebergs_info = after_icebergs_info

        # 다 녹아버렸으면 0 리턴
        return 0


if __name__ == '__main__':
    N: int
    M: int
    N, M = map(int, input().split())
    icebergs_info: list[list[int]] = [[int(x) for x in input().split()] for _ in range(N)]
    assert len(icebergs_info) == N
    assert len(icebergs_info[0]) == M
    s: Solution = Solution()
    print(s.solve(N, M, icebergs_info))
