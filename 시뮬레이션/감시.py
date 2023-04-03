from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, m: int, map_info: list[list[int]]) -> int:
        cameras: list[tuple[int, int]] = []

        for i in range(n):
            for j in range(m):
                if 1 <= map_info[i][j] <= 5:
                    cameras.append((i, j))

        # 카메라 1
        # 회전 0 (0,1)
        # 회전 1 (-1,0)
        # 회전 2 (0, -1)
        # 회전 3 (1, 0)
        # 카메라 2
        # 회전 0 (0, -1), (0, 1)
        # 회전 1 (-1, 0), (1, 0)
        # 회전 0 (0, -1), (0, 1)
        # 회전 0 (-1, 0), (1, 0)
        # 카메라 3
        # 회전 0 (0, 1), (-1, 0)
        # 회전 1 (-1, 0), (0, -1)
        # 회전 0 (0, -1), (1, 0)
        # 회전 0 (1, 0), (0, 1)
        # 카메라 4
        # 회전 0 (0, 1), (-1,0) , (0, -1)
        # 회전 1 (-1,0) , (0, -1), (1, 0)
        # 회전 0 (0, -1), (1, 0) (0, 1)
        # 회전 0 (1, 0) (0, 1), (-1, 0)
        # 카메라 5
        # 회전 상관 없이 (0, 1) , (-1, 0) (-1, 0) ( 1, 0)
        dy = [0, -1, 0, 1]
        dx = [1, 0, -1, 0]
        L: int = len(cameras)
        camera_directions: list[int] = [0] * L
        ans: int = m * n

        def dfs(l: int):
            nonlocal ans
            if l == L:
                # 카메라 시야 확인
                # 사각지대 카운팅 및 최솟값 업데이트
                tmp_map_info = [[y for y in x] for x in map_info]
                blind_cnt = 0
                for k in range(L):
                    y, x = cameras[k]
                    camera_num = map_info[y][x]
                    camera_num_direction = camera_directions[k]
                    if camera_num == 1:
                        q: deque = deque()
                        q.append(cameras[k])
                        while q:
                            y, x = q.popleft()
                            next_y = y + dy[camera_num_direction]
                            next_x = x + dx[camera_num_direction]
                            if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                                continue
                            if tmp_map_info[next_y][next_x] == 6:
                                continue
                            q.append((next_y, next_x))
                            tmp_map_info[next_y][next_x] = "#"
                    if camera_num == 2:
                        camera_num_direction %= 2
                        for i in range(2):
                            q: deque = deque()
                            q.append(cameras[k])
                            while q:
                                y, x = q.popleft()
                                next_y = y + dy[camera_num_direction + 2 * i]
                                next_x = x + dx[camera_num_direction + 2 * i]
                                if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                                    continue
                                if tmp_map_info[next_y][next_x] == 6:
                                    continue
                                q.append((next_y, next_x))
                                tmp_map_info[next_y][next_x] = "#"
                    if camera_num == 3:
                        for i in range(2):
                            q: deque = deque()
                            q.append(cameras[k])
                            while q:
                                y, x = q.popleft()
                                next_y = y + dy[(camera_num_direction + i) % 4]
                                next_x = x + dx[(camera_num_direction + i) % 4]
                                if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                                    continue
                                if tmp_map_info[next_y][next_x] == 6:
                                    continue
                                q.append((next_y, next_x))
                                tmp_map_info[next_y][next_x] = "#"
                    if camera_num == 4:
                        for i in range(3):
                            q: deque = deque()
                            q.append(cameras[k])
                            while q:
                                y, x = q.popleft()
                                next_y = y + dy[(camera_num_direction + i) % 4]
                                next_x = x + dx[(camera_num_direction + i) % 4]
                                if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                                    continue
                                if tmp_map_info[next_y][next_x] == 6:
                                    continue
                                q.append((next_y, next_x))
                                tmp_map_info[next_y][next_x] = "#"
                    if camera_num == 5:
                        for i in range(4):
                            q: deque = deque()
                            q.append(cameras[k])
                            while q:
                                y, x = q.popleft()
                                next_y = y + dy[i]
                                next_x = x + dx[i]
                                if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                                    continue
                                if tmp_map_info[next_y][next_x] == 6:
                                    continue
                                q.append((next_y, next_x))
                                tmp_map_info[next_y][next_x] = "#"

                # print("---")
                # for t in tmp_map_info:
                #     print(t)

                for i in range(n):
                    for j in range(m):
                        if tmp_map_info[i][j] == 0:
                            blind_cnt += 1

                ans = min(blind_cnt, ans)
                return

            for i in range(4):
                camera_directions[l] = i
                dfs(l + 1)

        dfs(0)

        return ans


if __name__ == "__main__":
    N: int
    M: int
    map_info: list[list[int]]
    N, M = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(N)]
    assert len(map_info) == N and len(map_info[0]) == M
    print(Solution.solve(N, M, map_info))
