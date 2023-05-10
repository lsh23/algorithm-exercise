global GROBAL_CNT
global GROBAL_ROUTE
global SY
global SX

GROBAL_CNT = 0
GROBAL_ROUTE = 999

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
s_dy = [0, -1, 0, 1, 0]
s_dx = [0, 0, -1, 0, 1]


class Fish:
    pass


class Fish:
    def __init__(self, y: int, x: int, d: int):
        self.y: int = y
        self.x: int = x
        self.d: int = d
        self.alive: bool = True

    def move(self, sy: int, sx: int, smell: list[list[int]], board: list[list[list[Fish]]]):
        d = self.d
        for i in range(8):
            d = (self.d - i) % 8
            ny = self.y + dy[d]
            nx = self.x + dx[d]
            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                continue
            if ny == sy and nx == sx:  # 상어가 있는 칸
                continue
            if smell[ny][nx] > 0:
                continue
            self.y = ny
            self.x = nx
            self.d = d
            break
        board[self.y][self.x].append(self)

    def __repr__(self):
        return f'({self.y},{self.x},{self.d})'


def shark_move(sy: int, sx: int, l: int, removed_cnt: int, route: list[int], board: list[list[list[Fish]]], smell: list[list[int]]):
    global GROBAL_CNT
    global GROBAL_ROUTE
    global SY
    global SX
    if l == 3:
        i_route = int(route[0]) * 100 + int(route[1]) * 10 + int(route[2])
        if removed_cnt > GROBAL_CNT:
            GROBAL_CNT = removed_cnt
            GROBAL_ROUTE = i_route
            SY, SX = sy, sx
        if removed_cnt == GROBAL_CNT:
            if i_route < GROBAL_ROUTE:
                GROBAL_ROUTE = i_route
                SY, SX = sy, sx

        return
    else:
        for i in range(1, 5):
            ny = sy + s_dy[i]
            nx = sx + s_dx[i]
            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                continue
            if len(board[ny][nx]) > 0 and smell[ny][nx] != 3:
                prev_smell = smell[ny][nx]
                smell[ny][nx] = 3
                for f in board[ny][nx]:
                    f.alive = False
                route[l] = i

                shark_move(ny, nx, l + 1, removed_cnt + len(board[ny][nx]), route, board, smell)

                for f in board[ny][nx]:
                    f.alive = True
                smell[ny][nx] = prev_smell
            else:
                route[l] = i
                shark_move(ny, nx, l + 1, removed_cnt, route, board, smell)

def update_board(board:list[list[int]], smell:list[list[int]]):
    ny = SY
    nx = SX
    s_route = str(GROBAL_ROUTE)

    if len(board[ny][nx]) > 0:
        smell[ny][nx] = 3
        for f in board[ny][nx]:
            f.alive = False

    for i in range(2):
        ny = ny + s_dy[int(s_route[2 - i])] * -1
        nx = nx + s_dx[int(s_route[2 - i])] * -1
        if len(board[ny][nx]) > 0:
            smell[ny][nx] = 3
            for f in board[ny][nx]:
                f.alive = False

class Solution:
    @staticmethod
    def solve(m: int, s: int, fish_info: list[list[int]], sy: int, sx: int) -> int:
        global GROBAL_CNT
        global GROBAL_ROUTE
        global SY
        global SX
        SY = sy
        SX = sx

        smell: list[list[int]] = [[0] * 4 for _ in range(4)]

        fishes: list[Fish] = []
        for fish in fish_info:
            fishes.append(Fish(fish[0], fish[1], fish[2]))

        for _ in range(s):
            # 0. 복제
            copied: list[Fish] = []
            for fish in fishes:
                copied.append(Fish(fish.y, fish.x, fish.d))

            board: list[list[list[Fish]]] = [[[] for _ in range(4)] for _ in range(4)]

            # 1. 모든 물고기가 한칸 이동한다.
            for fish in fishes:
                fish.move(SY, SX, smell, board)

            # 2. 상어가 연속해서 3칸 이동한다.
            GROBAL_CNT = 0
            GROBAL_ROUTE = 1000
            shark_move(SY, SX, 0, len(board[SY][SX]),[-1, -1, -1], board, smell)
            update_board(board, smell)

            # 3. 물고기 냄새 삭제
            for i in range(4):
                for j in range(4):
                    if smell[i][j] > 0:
                        smell[i][j] -= 1

            # 4. 복제 마법 완료
            for fish in fishes:
                if fish.alive == True:
                    copied.append(fish)

            fishes = copied

        return len(fishes)


if __name__ == "__main__":
    M: int
    S: int
    fish_info: list[list[int]]
    Sx: int
    Sy: int
    M, S = map(int, input().split())
    fish_info = [[int(x) - 1 for x in input().split()] for _ in range(M)]
    Sy, Sx = [int(x) - 1 for x in input().split()]
    print(Solution.solve(M, S, fish_info, Sy, Sx))