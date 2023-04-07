from collections import deque


def rotate(d: int, command: str):
    if command == 'L':
        return (d + 1) % 4
    if command == 'D':
        return (d + 3) % 4


def bound(y: int, x: int, n: int) -> bool:
    return 1 <= y <= n and 1 <= x <= n


class Solution:
    @staticmethod
    def solve(n: int, k: int, apple_loc: list[tuple[int, int]], l: int, snake_rotate_info: list[tuple[int, str]]):

        dy = [0, -1, 0, 1]
        dx = [1, 0, -1, 0]

        time: int = 0
        board: list[list[int]] = [[0] * (n + 1) for _ in range(n + 1)]
        # 게임판에 사과 배치
        for a in apple_loc:
            a_y, a_x = a
            board[a_y][a_x] = 2

        snake: deque[tuple[int, int]] = deque()

        d = 0
        s_y, s_x = 1, 1
        snake.append((s_y, s_x))
        board[s_y][s_x] = 1

        while True:
            time += 1

            # 1. 몸 길이를 늘려서 머리를 다음 칸에 위치시킨다
            next_y = s_y + dy[d]
            next_x = s_x + dx[d]
            if not bound(next_y, next_x, n) or board[next_y][next_x] == 1:
                break
            # 2. 이동한 칸에 사과가 있으면, 그칸에 있는 사과는 없어진다
            # 3. 사과가 없으면,          몸 길이를 줄여서 꼬리가 위치한 칸을 비워준다.
            if board[next_y][next_x] != 2:
                tail_y, tail_x = snake.popleft()
                board[tail_y][tail_x] = 0
            if time in snake_rotate_info:
                command = snake_rotate_info[time]
                d = rotate(d, command)

            snake.append((next_y, next_x))
            board[next_y][next_x] = 1
            s_y = next_y
            s_x = next_x

        return time


if __name__ == "__main__":
    N: int
    K: int
    L: int
    apple_loc: list[tuple[int, int]]
    snake_rotate_info: dict[int, str]

    N = int(input())
    K = int(input())
    apple_loc = [tuple(map(int, input().split())) for _ in range(K)]
    L = int(input())
    snake_rotate_info = {}
    for _ in range(L):
        X, C = input().split()
        snake_rotate_info[int(X)] = C

    print(Solution.solve(N, K, apple_loc, L, snake_rotate_info))
