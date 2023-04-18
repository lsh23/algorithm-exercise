class Solution:
    @staticmethod
    def solve(n: int, m: int, t: int, board: list[list[int]], rotate: list[list[int]]) -> int:

        for i in range(t):
            x, d, k = rotate[i]
            # 회전
            # d가 0 이면 시계방향  ->
            # d가 1 이면 반시계 방향 <-
            for r in range(x, n + 1, x):
                tmp_board: list[int] = [0] * m
                for c in range(m):
                    if d == 0:
                        tmp_board[c] = board[r - 1][(c - k) % m]
                    if d == 1:
                        tmp_board[c] = board[r - 1][(c + k) % m]
                board[r - 1] = tmp_board

            # 회전 후 연산
            dr = [0, -1, 0, 1]
            dc = [1, 0, -1, 0]
            check: list[list[int]] = [[0] * m for _ in range(n)]
            is_same_number_adjacent: bool = False
            total: int = 0
            cnt: int = 0
            for r in range(n):
                for c in range(m):
                    # 인접하면서 수가 같은 걸 찾는다
                    # 현재 칸의 숫자
                    if board[r][c] == 0:
                        continue
                    cnt_same_number_adjacent: int = 0
                    total += board[r][c]
                    cnt += 1
                    for j in range(4):
                        nr = r + dr[j]
                        nc = (c + dc[j]) % m
                        if nr < 0 or nr >= n:
                            continue
                        if board[nr][nc] == board[r][c]:
                            is_same_number_adjacent = True
                            cnt_same_number_adjacent += 1
                            check[nr][nc] = 1
                    if cnt_same_number_adjacent > 0:
                        check[r][c] = 1

            # print("----check----")
            # for c in check:
            #     print(c)

            if total == 0:
                break

            if is_same_number_adjacent:
                for r in range(n):
                    for c in range(m):
                        if check[r][c] == 1:
                            board[r][c] = 0
            else:
                avg = total / cnt
                for r in range(n):
                    for c in range(m):
                        if board[r][c] == 0:
                            continue
                        if board[r][c] > avg:
                            board[r][c] -= 1
                        elif board[r][c] < avg:
                            board[r][c] += 1
            # print("---baord---")
            # for b in board:
            #     print(b)

        return sum([sum(x) for x in board])


if __name__ == "__main__":
    N: int
    M: int
    T: int
    board: list[list[int]]
    rotate: list[list[int]]
    N, M, T = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    rotate = [[int(x) for x in input().split()] for _ in range(T)]
    print(Solution.solve(N, M, T, board, rotate))
