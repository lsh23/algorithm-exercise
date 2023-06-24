def find_heart(n: int, board: list[list[str]]) -> tuple[int, int]:
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if board[i - 1][j] == "*" and board[i + 1][j] == "*" \
                    and board[i][j - 1] == "*" and board[i][j + 1] == "*":
                return (i, j)


def get_left_arm_length(heart_y: int, heart_x: int, n: int, board: list[list[str]]) -> int:
    ny = heart_y
    nx = heart_x
    left_arm_length: int = 0
    while True:
        ny = ny
        nx = nx - 1
        if nx < 0:
            break
        if board[ny][nx] != "*":
            break
        left_arm_length += 1
    return left_arm_length


def get_right_arm_length(heart_y: int, heart_x: int, n: int, board: list[list[str]]) -> int:
    ny = heart_y
    nx = heart_x
    right_arm_length: int = 0
    while True:
        ny = ny
        nx = nx + 1
        if nx >= n:
            break
        if board[ny][nx] != "*":
            break
        right_arm_length += 1
    return right_arm_length


def get_waist_length(heart_y: int, heart_x: int, n: int, board: list[list[str]]) -> int:
    ny = heart_y
    nx = heart_x
    waist_length: int = 0
    while True:
        ny = ny + 1
        nx = nx
        if ny >= n:
            break
        if board[ny][nx] != "*":
            break
        waist_length += 1
    return waist_length


def get_left_leg_length(heart_y: int, heart_x: int, waist_length: int, n: int, board: list[list[str]]) -> int:
    ny = heart_y + waist_length + 1
    nx = heart_x - 1
    left_leg_length: int = 1
    while True:
        ny = ny + 1
        nx = nx
        if ny >= n:
            break
        if board[ny][nx] != "*":
            break
        left_leg_length += 1
    return left_leg_length


def get_right_leg_length(heart_y: int, heart_x: int, waist_length: int, n: int, board: list[list[str]]) -> int:
    ny = heart_y + waist_length + 1
    nx = heart_x + 1
    right_leg_length: int = 1
    while True:
        ny = ny + 1
        nx = nx
        if ny >= n:
            break
        if board[ny][nx] != "*":
            break
        right_leg_length += 1
    return right_leg_length


class Solution:
    @staticmethod
    def solve(n: int, board: list[list[str]]):
        heart_y, heart_x = find_heart(n, board)

        left_arm_length = get_left_arm_length(heart_y, heart_x, n, board)
        right_arm_length = get_right_arm_length(heart_y, heart_x, n, board)
        waist_length = get_waist_length(heart_y, heart_x, n, board)
        left_leg_length = get_left_leg_length(heart_y, heart_x, waist_length, n, board)
        right_leg_length = get_right_leg_length(heart_y, heart_x, waist_length, n, board)

        print(heart_y + 1, heart_x + 1)
        print(left_arm_length, right_arm_length, waist_length, left_leg_length, right_leg_length)


if __name__ == "__main__":
    N: int
    board: list[list[str]]
    N = int(input())
    board = [[x for x in input()] for _ in range(N)]
    Solution.solve(N, board)
