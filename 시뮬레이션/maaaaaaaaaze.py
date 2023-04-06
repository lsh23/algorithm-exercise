from itertools import permutations
from collections import deque


def rotate_board(cnt:int, board:list[list[int]]) -> list[list[int]]:
    rotated_board = [[x for x in y] for y in board]

    for k in range(cnt):
        for i in range(5):
            for j in range(5):
                rotated_board[j][5-i-1] = board[i][j]
        board = [[x for x in y] for y in rotated_board]

    return rotated_board


class Solution:
    @staticmethod
    def solve(board: list[list[list[int]]]) -> int:

        ans: int = 251

        dz = [0, 0, 0, 0, -1, 1]
        dy = [0, -1, 0, 1, 0, 0]
        dx = [1, 0, -1, 0, 0, 0]

        for i in range(1024):
            rotate = ""
            while i:
                rotate += str(i % 4)
                i //= 4
            rotate = rotate[::-1]
            rotate = rotate.zfill(5)

            # 각 판 회전
            rotated_board = [[[x for x in y] for y in z] for z in board]

            for k in range(5):
                rotated_board[k] = rotate_board(int(rotate[k]), rotated_board[k])

            for order in permutations([0, 1, 2, 3, 4]):
                # 판을 쌓는다
                miro: list[list[list[int]]] = [[] for _ in range(5)]
                dist: list[list[list[int]]] = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
                for k in range(5):
                    miro[k] = rotated_board[order[k]]
                # bfs로 탈출여부 및 최소 이동 횟수 구하기


                # print("------")
                # for m in miro:
                #     print(m)

                if miro[0][0][0] != 1:
                    continue

                start: tuple[int, int, int] = (0, 0, 0)
                dist[0][0][0] = 0
                q: deque[tuple[int, int, int]] = deque()
                q.append(start)
                while q:
                    z, y, x = q.popleft()
                    if z == 4 and y == 4 and x == 4:
                        ans = min(ans, dist[z][y][x])
                        break
                    for k in range(6):
                        next_z = z + dz[k]
                        next_y = y + dy[k]
                        next_x = x + dx[k]
                        if next_z < 0 or next_z >= 5 or next_y < 0 or next_y >= 5 or next_x < 0 or next_x >= 5:
                            continue
                        if miro[next_z][next_y][next_x] != 1:
                            continue
                        if dist[next_z][next_y][next_x] != -1:
                            continue
                        q.append((next_z, next_y, next_x))
                        dist[next_z][next_y][next_x] = dist[z][y][x] + 1

        if ans == 251:
            return -1
        return ans


if __name__ == "__main__":
    board: list[list[list[int]]] = [[] for _ in range(5)]
    for i in range(5):
        board[i] = [[int(x) for x in input().split()] for _ in range(5)]
    assert len(board) == 5 and len(board[0]) == 5 and len(board[0][0]) == 5
    print(Solution.solve(board))
