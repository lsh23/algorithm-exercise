from collections import deque

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


class Solution:
    @staticmethod
    def solve(n: int, m: int, fuel: int, map_info: list[list[int]], start_y: int, start_x: int,
              drive_info: list[list[int]]) -> int:
        check: list[int] = [0] * m

        # 1. 현재 택시 위치에서 가장 가까운 손님의 위치를 구한다.
        #      그런 승객이 여러 명이면 그 중에 행번호가 가장 작은 승객을, 행번호도 같으면  열번호가 작은 승객을 고른다
        #      현재 택시와 승객이 같은 위치에 서있으면 최단거리는
        #     현재 택시 위치에서 BFS O(N*N)
        #     check[i] == 0인 drive_info[i] 를 대상으로 다음 손님위치를 구한다.
        while True:
            q: deque[tuple[int, int]] = deque()
            dist: list[list[int]] = [[-1] * n for _ in range(n)]
            dist[start_y][start_x] = 0
            q.append((start_y, start_x))
            while q:
                y, x = q.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue
                    if map_info[ny][nx] == 1:
                        continue
                    if dist[ny][nx] != -1:
                        continue
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

            next_drive: int = -1
            next_start_y: int = 0
            next_start_x: int = 0
            dist_to_next_start: int = 401
            for i in range(m):
                if check[i] != 0:
                    continue
                s_y, s_x, d_y, d_x = drive_info[i]
                d = dist[s_y][s_x]
                if d == -1:
                    continue
                if dist_to_next_start > d:
                    dist_to_next_start = d
                    next_start_y = s_y
                    next_start_x = s_x
                    next_drive = i
                elif dist_to_next_start == d:
                    if next_start_y > s_y:
                        next_start_y = s_y
                        next_start_x = s_x
                        next_drive = i
                    elif next_start_y == s_y:
                        if next_start_x > s_x:
                            next_start_y = s_y
                            next_start_x = s_x
                            next_drive = i

            if next_drive == -1:
                return -1

            fuel -= dist_to_next_start

            # 2. 그 승객의 목적지로 이동하고, 이동하면서 소모한 연료 양의 2배가 충전된다. 이동 와중에 연료가 떨어지면 이동 실패,

            dist = [[-1] * n for _ in range(n)]
            dist[next_start_y][next_start_x] = 0
            q.append((next_start_y, next_start_x))
            while q:
                y, x = q.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue
                    if map_info[ny][nx] == 1:
                        continue
                    if dist[ny][nx] != -1:
                        continue
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

            s_y, s_x, d_y, d_x = drive_info[next_drive]
            if dist[d_y][d_x] == -1:
                return -1
            if fuel >= dist[d_y][d_x]:
                fuel += dist[d_y][d_x]
                start_y = d_y
                start_x = d_x
                check[next_drive] = 1
            else:
                fuel -= dist[d_y][d_x]
                break

            if all(x == 1 for x in check):
                break

        # 3.최종적으로 남은 연료의 양을 출력 // 실패하면 -1
        if fuel < 0:
            return -1
        else:
            return fuel


if __name__ == "__main__":
    N: int
    M: int
    fuel: int
    map_info: list[list[int]]
    start_y: int
    start_x: int
    drive_info: list[list[int]]

    N, M, fuel = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(N)]
    start_y, start_x = [int(x) - 1 for x in input().split()]
    drive_info = [[int(x) - 1 for x in input().split()] for _ in range(M)]

    print(Solution.solve(N, M, fuel, map_info, start_y, start_x, drive_info))
