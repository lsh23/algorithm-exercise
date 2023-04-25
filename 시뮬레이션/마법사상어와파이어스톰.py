from collections import deque

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def divide_and_rotate(a: list[list[int]], n: int, _l: int):
    for i in range(0, 2 ** n, 2 ** _l):
        for j in range(0, 2 ** n, 2 ** _l):
            rotate(i, j, 2 ** _l, a)


def rotate(start_y: int, start_x: int, n: int, a: list[list[int]]) -> None:
    tmp_a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp_a[i][j] = a[start_y + i][start_x + j]

    for i in range(n):
        for j in range(n):
            a[start_y + j][start_x + n - 1 - i] = tmp_a[i][j]


def melting_ice(a: list[list], n: int) -> list[list[int]]:
    after_a = [[0] * (2 ** n) for _ in range(2 ** n)]
    for i in range(2 ** n):
        for j in range(2 ** n):
            adjacent_ice: int = 0
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if ny < 0 or ny >= 2 ** n or nx < 0 or nx >= 2 ** n:
                    continue
                if a[ny][nx] > 0:
                    adjacent_ice += 1
            if adjacent_ice < 3:
                after_a[i][j] = a[i][j] - 1
            else:
                after_a[i][j] = a[i][j]
    return after_a


def check_ice(a: list[list[int]], n: int):
    cnt: int = 0  # 남아있는 얼음의 합
    max_size: int = 0  # 가장 큰 덩어리
    visited: list[list[int]] = [[0] * (2 ** n) for _ in range(2 ** n)]
    for i in range(2 ** n):
        for j in range(2 ** n):
            if a[i][j] <= 0:
                continue
            cnt += a[i][j]
            if visited[i][j] != 0:
                continue
            visited[i][j] = 1
            size: int = 1
            q: deque[tuple[int, int]] = deque()
            q.append((i, j))
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if ny < 0 or ny >= 2 ** n or nx < 0 or nx >= 2 ** n:
                        continue
                    if visited[ny][nx] != 0:
                        continue
                    if a[ny][nx] < 1:
                        continue
                    visited[ny][nx] = 1
                    size += 1
                    q.append((ny, nx))

            max_size = max(size, max_size)
    print(cnt)
    print(max_size)


class Solution:
    @staticmethod
    def solve(n: int, q: int, a: list[list[int]], l: list[int]) -> None:
        for _l in l:
            # 2**k 로 배열 나누고 돌리기 
            divide_and_rotate(a, n, _l)

            # 얼음의 양 줄이기
            a = melting_ice(a, n)

        check_ice(a, n)


if __name__ == "__main__":
    N: int
    Q: int
    A: list[list[int]]
    L: list[int]
    N, Q = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(2 ** N)]
    L = [int(x) for x in input().split()]
    Solution.solve(N, Q, A, L)
