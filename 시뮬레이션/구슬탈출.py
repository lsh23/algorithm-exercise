from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, m: int, board: list[list[int]]) -> int:
        ans: int = -1
        b: tuple[int, int]
        r: tuple[int, int]
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'B':
                    b = (i, j)
                if board[i][j] == 'R':
                    r = (i, j)

        dy = [0, -1, 0, 1]
        dx = [1, 0, -1, 0]

        visited: list[list[list[list[int]]]] = [[[[0] * 10 for _ in range(10)] for _ in range(10)] for _ in range(10)]
        assert len(visited) == 10 and len(visited[0]) == 10 and len(visited[0][0]) == 10 and len(visited[0][0][0]) == 10

        b_y, b_x = b
        r_y, r_x = r

        visited[b_y][b_x][r_y][r_x] = 1
        q: deque[tuple[int, int, int, int]] = deque()
        q.append((b_y, b_x, r_y, r_x, 0))

        while q:
            b_y, b_x, r_y, r_x, cnt = q.popleft()
            # print(b_y, b_x, r_y, r_x)
            if board[r_y][r_x] == 'O' and board[b_y][b_x] != 'O':
                ans = cnt
                break
            if cnt > 10:
                break
            for i in range(4):
                next_b_y = b_y
                next_b_x = b_x
                while True:
                    if next_b_y + dy[i] < 0 or next_b_y + dy[i] >= n or next_b_x + dx[i] < 0 or next_b_x + dx[i] >= m:
                        break
                    if board[next_b_y + dy[i]][next_b_x + dx[i]] == '#':
                        break
                    next_b_y = next_b_y + dy[i]
                    next_b_x = next_b_x + dx[i]
                    if board[next_b_y][next_b_x] == 'O':
                        break

                next_r_y = r_y
                next_r_x = r_x
                while True:
                    if next_r_y + dy[i] < 0 or next_r_y + dy[i] >= n or next_r_x + dx[i] < 0 or next_r_x + dx[i] >= m:
                        break
                    if board[next_r_y + dy[i]][next_r_x + dx[i]] == '#':
                        break
                    next_r_y = next_r_y + dy[i]
                    next_r_x = next_r_x + dx[i]
                    if board[next_r_y][next_r_x] == 'O':
                        break

                if visited[next_b_y][next_b_x][next_r_y][next_r_x] != 0:
                    continue

                if board[next_b_y][next_b_x] == 'O':
                    continue

                if next_b_y == next_r_y and next_b_x == next_r_x:
                    b_dist = abs(b_y - next_b_y) + abs(b_x - next_b_x)
                    r_dist = abs(r_y - next_r_y) + abs(r_x - next_r_x)
                    if b_dist < r_dist:
                        next_r_y -= dy[i]
                        next_r_x -= dx[i]
                    else:
                        next_b_y -= dy[i]
                        next_b_x -= dx[i]

                visited[next_b_y][next_b_x][next_r_y][next_r_x] = 1
                q.append((next_b_y, next_b_x, next_r_y, next_r_x, cnt + 1))
        return ans


if __name__ == "__main__":
    N: int
    M: int
    board: list[list[int]]
    N, M = map(int, input().split())
    board = [[x for x in input()] for _ in range(N)]
    assert len(board) == N and len(board[0]) == M
    print(Solution.solve(N, M, board))
