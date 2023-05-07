from collections import deque

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


# d    0  1   2  3

def rotate(dice: list[int], direction: int):
    if direction == 0:
        return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]

    if direction == 1:
        return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

    if direction == 2:
        return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

    if direction == 3:
        return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]


def get_score(y: int, x: int, map_info: list[list[int]]) -> int:
    number = map_info[y][x]
    cnt: int = 1
    n = len(map_info)
    m = len(map_info[0])
    visited: list[list[int]] = [[0] * m for _ in range(n)]
    q: deque[tuple[int, int]] = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx] != 0:
                continue
            if map_info[ny][nx] != number:
                continue
            visited[ny][nx] = 1
            q.append((ny, nx))
            cnt += 1

    return number * cnt


def get_next_direction(a: int, b: int, direction: int) -> int:
    if a > b:
        return (direction - 1) % 4
    if a < b:
        return (direction + 1) % 4
    if a == b:
        return direction


class Solution:
    @staticmethod
    def solve(n: int, m: int, k: int, map_info: list[list[int]]) -> int:

        # 2. 주사위가 도착한 칸에 대한 점수를 획득 한다.
        # 3. 주사위의 아랫면에 있는 정수와 주사위가 있는 칸에 있는 정수를 비교 해서 이동 방향을 결정한다.
        score: int = 0
        dice: list[int] = [1, 2, 3, 4, 5, 6]  # dice[5] 이 아랫면
        direction: int = 0
        y: int = 0
        x: int = 0
        for i in range(k):
            # 1. 주사위를 이동 방향으로 한칸 굴린다.
            # 이동 방향에 칸이 없으면, 방향을 반대로 하고 한칸 굴린다.
            ny = y + dy[direction]
            nx = x + dx[direction]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                direction = (direction + 2) % 4
                ny = y + dy[direction]
                nx = x + dx[direction]
            dice = rotate(dice, direction)
            score += get_score(ny, nx, map_info)

            A = dice[5]
            B = map_info[ny][nx]
            direction = get_next_direction(A, B, direction)
            y = ny
            x = nx

        return score


if __name__ == "__main__":
    N: int
    M: int
    K: int
    map_info: list[list[int]]
    N, M, K = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, M, K, map_info))
