dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


class Solution:

    @staticmethod
    def solve(n: int, k: int, board_info: list[list[int]], chess_pieces: list[list[int]]) -> int:
        cnt: int = 0

        board: list[list[list[int]]] = [[[] for _ in range(n)] for _ in range(n)]

        for i in range(k):
            y, x, d = chess_pieces[i]
            chess_pieces[i] = [y, x, d, 0]
            board[y][x].append(i)

        while cnt <= 1000:
            cnt += 1

            for i in range(k):
                y, x, d, h = chess_pieces[i]
                ny = y + dy[d]
                nx = x + dx[d]
                if (ny < 0 or ny >= n or nx < 0 or nx >= n) or board_info[ny][nx] == 2:
                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    else:
                        d = 2
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        chess_pieces[i] = [y, x, d, h]
                        continue
                    if board_info[ny][nx] == 2:
                        chess_pieces[i] = [y, x, d, h]
                        continue
                    chess_pieces[i] = [y, x, d, h]

                if board_info[ny][nx] == 0:
                    if len(board[ny][nx]) == 0:
                        board[ny][nx] = board[y][x][h:]
                    else:
                        board[ny][nx] += board[y][x][h:]
                    for j in range(len(board[ny][nx])):
                        t_y, t_x, t_d, t_h = chess_pieces[board[ny][nx][j]]
                        chess_pieces[board[ny][nx][j]] = [ny, nx, t_d, j]
                    board[y][x] = board[y][x][:h]

                elif board_info[ny][nx] == 1:
                    if len(board[ny][nx]) == 0:
                        board[ny][nx] = board[y][x][h:][::-1]
                    else:
                        board[ny][nx] += board[y][x][h:][::-1]
                    for j in range(len(board[ny][nx])):
                        t_y, t_x, t_d, t_h = chess_pieces[board[ny][nx][j]]
                        chess_pieces[board[ny][nx][j]] = [ny, nx, t_d, j]
                    board[y][x] = board[y][x][:h]

                if len(board[ny][nx]) >= 4:
                    return cnt

        return -1


if __name__ == "__main__":
    N: int
    K: int
    board_info: list[list[int]]
    chess_pieces: list[list[int]]
    N, K = map(int, input().split())
    board_info = [[int(x) for x in input().split()] for _ in range(N)]
    chess_pieces = [[int(x) - 1 for x in input().split()] for _ in range(K)]
    print(Solution.solve(N, K, board_info, chess_pieces))
