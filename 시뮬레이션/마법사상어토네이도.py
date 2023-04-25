dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

s_dy = [
    [-1, -1, -1, 1, 1, 1, -2, 2, 0],
    [1, 0, -1, 1, 0, -1, 0, 0, 2],
    [-1, -1, -1, 1, 1, 1, -2, 2, 0],
    [-1, 0, 1, -1, 0, 1, 0, 0, -2],
]
s_dx = [
    [-1, 0, 1, -1, 0, 1, 0, 0, -2],
    [-1, -1, -1, 1, 1, 1, -2, 2, 0],
    [1, 0, -1, 1, 0, -1, 0, 0, 2],
    [-1, -1, -1, 1, 1, 1, -2, 2, 0],
]
ratio = [10, 7, 1, 10, 7, 1, 2, 2, 5]


class Solution:
    @staticmethod
    def solve(n: int, a: list[list[int]]) -> int:
        ans: int = 0

        y: int = n // 2
        x: int = n // 2
        d: int = -1
        l: int = 0
        cnt: int = 0
        while True:
            # 토네이도 이동
            d = (d + 1) % 4
            if cnt % 2 == 0:
                l += 1
            for i in range(l):
                ny = y + dy[d]
                nx = x + dx[d]
                if y == 0 and x == -1:
                    break

                # 흩날림
                if a[ny][nx] == 0:
                    y = ny
                    x = nx
                    continue
                next_a = a[ny][nx]

                for k in range(9):
                    s_ny = ny + s_dy[d][k]
                    s_nx = nx + s_dx[d][k]
                    s = (a[ny][nx] * ratio[k]) // 100
                    next_a -= s
                    if s_ny < 0 or s_ny >= n or s_nx < 0 or s_nx >= n:  # 격자 밖으로 나간 경우
                        ans += s
                        continue
                    a[s_ny][s_nx] += s

                if ny + dy[d] < 0 or ny + dy[d] >= n or nx + dx[d] < 0 or nx + dx[d] >= n:
                    ans += next_a
                else:
                    a[ny + dy[d]][nx + dx[d]] += next_a

                a[ny][nx] = 0

                y = ny
                x = nx

            if y == 0 and x == -1:
                break

            cnt += 1

        return ans


if __name__ == "__main__":
    N: int
    A: list[list[int]]
    N = int(input())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, A))
