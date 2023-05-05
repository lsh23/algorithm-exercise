dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]


class Solution:
    @staticmethod
    def solve(n: int, m: int, A: list[list[int]], move_info: list[list[int]]) -> int:
        # N*N 격자
        # 구름 배열

        clouds: list[tuple[int, int]] = []

        clouds.append((n - 1, 0))
        clouds.append((n - 1, 1))
        clouds.append((n - 2, 0))
        clouds.append((n - 2, 1))

        for move in move_info:
            is_cloud: list[list[int]] = [[0] * n for _ in range(n)]
            d, s = move
            rain_blocks: list[tuple[int, int]] = []
            for cloud in clouds:
                # 이동 후 물의양 증가
                # 물이 증가한 칸 저장
                y, x = cloud
                ny = (y + (dy[d - 1]) * s) % n
                nx = (x + (dx[d - 1]) * s) % n
                A[ny][nx] += 1
                rain_blocks.append((ny, nx))
                is_cloud[ny][nx] = 1

            # 물이 증가한 칸에 대해서 물복사 버그 진행
            for block in rain_blocks:
                y, x = block
                adj_water_cnt: int = 0
                for d in [1, 3, 5, 7]:
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue
                    if A[ny][nx] == 0:
                        continue
                    adj_water_cnt += 1
                A[y][x] += adj_water_cnt

            next_clouds: list[tuple[int, int]] = []

            # 바구니의 저장된 물이 2이상인 모든칸에 대해 구름 생성 및 물의 양 2 감소, 이때 구름이 생기는 칸은 구름이 사라진 칸이 아니여야함
            for i in range(n):
                for j in range(n):
                    if A[i][j] < 2:
                        continue
                    if is_cloud[i][j] == 1:
                        continue
                    A[i][j] -= 2
                    next_clouds.append((i, j))

            clouds = next_clouds

        ans: int = 0
        for i in range(n):
            for j in range(n):
                ans += A[i][j]

        return ans


if __name__ == "__main__":
    N: int
    M: int
    A: list[list[int]]
    move_info: list[list[int]]
    N, M = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    move_info = [[int(x) for x in input().split()] for _ in range(M)]
    print(Solution.solve(N, M, A, move_info))
