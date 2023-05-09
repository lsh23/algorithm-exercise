from collections import deque

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]
h_dy = [
    [],
    [0, -1, 1],
    [0, -1, 1],
    [-1, -1, -1],
    [1, 1, 1],
]

h_dx = [
    [],
    [1, 1, 1],
    [-1, -1, -1],
    [0, -1, 1],
    [0, -1, 1],
]


def heater_on(heater: tuple[int, int, int], room_info: list[list[int]], wall_info: list[list[list[list[int]]]]):
    q: deque[tuple[int, int, int]] = deque()
    y, x, d = heater
    y = y + dy[d]
    x = x + dx[d]
    if y < 0 or y >= R or x < 0 or x >= C:
        return

    q.append((y, x, 5))
    visited: list[list[int]] = [[0] * C for _ in range(R)]
    visited[y][x] = 1
    while q:
        y, x, t = q.popleft()
        room_info[y][x] += t
        if t == 1:  # 처리안하면 음수전파가 됨 5->4->3->2->1->0->-1
            continue
        for i in range(3):
            ny = y + h_dy[d][i]
            nx = x + h_dx[d][i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if d == 3 or d == 4:
                if x == nx:
                    if wall_info[y][x][ny][nx] == 1:
                        continue
                else:
                    if wall_info[y][x][y][nx] == 1 or wall_info[y][nx][ny][nx] == 1:
                        continue
            if d == 1 or d == 2:
                if y == ny:
                    if wall_info[y][x][ny][nx] == 1:
                        continue
                else:
                    if wall_info[y][x][ny][x] == 1 or wall_info[ny][x][ny][nx] == 1:
                        continue
            if visited[ny][nx] != 0:
                continue
            visited[ny][nx] = 1
            q.append((ny, nx, t - 1))


def adjust_temperature(room_info: list[list[int]], wall_info: list[list[list[list[int]]]]) -> list[list[int]]:
    adjusted: list[list[int]] = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            cur_t: int = room_info[i][j]
            if cur_t == 0:
                continue
            adjusted[i][j] += cur_t
            for k in range(1, 5):
                ny = i + dy[k]
                nx = j + dx[k]
                if ny < 0 or ny >= R or nx < 0 or nx >= C:
                    continue
                if wall_info[i][j][ny][nx] == 1:
                    continue
                if room_info[ny][nx] < cur_t:
                    adjusted[i][j] -= (cur_t - room_info[ny][nx]) // 4
                    adjusted[ny][nx] += (cur_t - room_info[ny][nx]) // 4

    return adjusted


class Solution:
    @staticmethod
    def solve(r: int, c: int, k: int, w: int, room_info: list[list[int]],
              wall_info: list[list[list[list[int]]]]) -> int:
        ans: int = 0
        heater: list[tuple[int, int, int]] = []
        target: list[tuple[int, int]] = []
        for i in range(r):
            for j in range(c):
                if 1 <= room_info[i][j] <= 4:
                    heater.append((i, j, room_info[i][j]))
                    room_info[i][j] = 0
                if room_info[i][j] == 5:
                    target.append((i, j))
                    room_info[i][j] = 0

        # 1. 온풍기 바람 나옴
        while ans <= 100:

            if ans == 100:  # 초콜렛을 100개 먹고도 안끝난 경우
                ans = 101
                break

            for h in heater:
                heater_on(h, room_info, wall_info)

            # 2. 온도 조절
            room_info = adjust_temperature(room_info, wall_info)

            # 3. 온도가 1이상인 가장 바깥쪽 칸의 온도가 1 감소
            for i in range(r):
                for j in range(c):
                    if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                        if room_info[i][j] > 0:
                            room_info[i][j] -= 1

            # 4. 초콜릿 하나 먹는다
            ans += 1

            # 5. 조사하는 칸의 온도가 K이상이 되었는지 검사
            if all([room_info[tg[0]][tg[1]] >= k for tg in target]):
                # for rm in room_info:
                #     print(*rm, sep=" ")
                break

        return ans


if __name__ == "__main__":
    R: int
    C: int
    K: int
    W: int
    room_info: list[list[int]]
    wall_info: list[list[list[list[int]]]]
    R, C, K = map(int, input().split())
    room_info = [[int(x) for x in input().split()] for _ in range(R)]
    wall_info = [[[[0] * C for _ in range(R)] for _ in range(C)] for _ in range(R)]
    W = int(input())
    for _ in range(W):
        y, x, t = map(int, input().split())
        y = y - 1
        x = x - 1
        if t == 0:
            if y - 1 < 0:
                continue
            wall_info[y][x][y - 1][x] = 1
            wall_info[y - 1][x][y][x] = 1
        if t == 1:
            if x + 1 >= C:
                continue
            wall_info[y][x][y][x + 1] = 1
            wall_info[y][x + 1][y][x] = 1
    print(Solution.solve(R, C, K, W, room_info, wall_info))
