from collections import deque


class Solution:
    @staticmethod
    def solve(r: int, c: int, t: int, A_r_c: list[list[int]]) -> int:
        ans: int = 0

        dy = [0, -1, 0, 1]
        dx = [1, 0, -1, 0]

        cleaner: list[tuple[int, int]] = []
        for i in range(r):
            for j in range(c):
                if A_r_c[i][j] == -1:
                    cleaner.append((i, j))
        # T초 동안
        for _ in range(t):
            tmp_A_r_c = [[0] * c for _ in range(r)]
            # 1. 미세먼지 확산 - BFS
            dust: list[tuple[int, int]] = []
            for i in range(r):
                for j in range(c):
                    if A_r_c[i][j] != -1 and A_r_c[i][j] != 0:
                        dust.append((i, j))
            q: deque[tuple[int, int]] = deque(dust)
            while q:
                y, x = q.popleft()
                cnt: int = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= r or nx < 0 or nx >= c:
                        continue
                    if A_r_c[ny][nx] == -1:
                        continue
                    cnt += 1
                    tmp_A_r_c[ny][nx] += (A_r_c[y][x] // 5)
                tmp_A_r_c[y][x] += (A_r_c[y][x]) - ((A_r_c[y][x] // 5) * cnt)

            # print("확산")
            # for z in tmp_A_r_c:
            #     print(z)

            # 2. 공기청정기에 의한 미세먼지 이동
            # 위쪽 공기 청정기 cleaner[0] (y,x)
            y, x = cleaner[0]
            u_dy = [0, -1, 0, 1]
            u_dx = [1, 0, -1, 0]
            d = 0
            prev_dust = 0
            ny = y
            nx = x
            tmp_A_r_c[y][x] = -1
            while True:
                # print(d)
                ny = ny + u_dy[d]
                nx = nx + u_dx[d]
                if ny < 0 or ny >= r or nx < 0 or nx >= c:
                    ny = ny - u_dy[d]
                    nx = nx - u_dx[d]
                    d += 1
                    continue
                if ny == y and nx == x:
                    break
                tmp = tmp_A_r_c[ny][nx]
                tmp_A_r_c[ny][nx] = prev_dust
                prev_dust = tmp
            # 아래쪽 공기 청정기 cleaner[1] (y,x)
            y, x = cleaner[1]
            d_dy = [0, 1, 0, -1]
            d_dx = [1, 0, -1, 0]
            d = 0
            prev_dust = 0
            ny = y
            nx = x
            tmp_A_r_c[y][x] = -1
            while True:
                # print(d)
                ny = ny + d_dy[d]
                nx = nx + d_dx[d]
                if ny < 0 or ny >= r or nx < 0 or nx >= c:
                    ny = ny - d_dy[d]
                    nx = nx - d_dx[d]
                    d += 1
                    continue
                if ny == y and nx == x:
                    break
                tmp = tmp_A_r_c[ny][nx]
                tmp_A_r_c[ny][nx] = prev_dust
                prev_dust = tmp

            # print("이동")
            # for z in tmp_A_r_c:
            #     print(z)
            A_r_c = tmp_A_r_c
        # 남아있는 미세먼지의양
        for i in range(r):
            for j in range(c):
                if A_r_c[i][j] != -1 and A_r_c[i][j] != 0:
                    ans += A_r_c[i][j]
        return ans


if __name__ == "__main__":
    R: int
    C: int
    T: int
    A_r_c: list[list[int]]
    R, C, T = map(int, input().split())
    A_r_c = [[int(x) for x in input().split()] for _ in range(R)]
    print(Solution.solve(R, C, T, A_r_c))
