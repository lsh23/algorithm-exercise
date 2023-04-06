def rotate(direction: int, dice: list[int]):
    tmp_dice = [x for x in dice]
    if direction == 1:
        dice[4] = tmp_dice[1]
        dice[1] = tmp_dice[5]
        dice[3] = tmp_dice[4]
        dice[5] = tmp_dice[3]
    if direction == 2:
        dice[4] = tmp_dice[3]
        dice[1] = tmp_dice[4]
        dice[3] = tmp_dice[5]
        dice[5] = tmp_dice[1]
    if direction == 3:
        dice[0] = tmp_dice[3]
        dice[1] = tmp_dice[0]
        dice[2] = tmp_dice[1]
        dice[3] = tmp_dice[2]
    if direction == 4:
        dice[0] = tmp_dice[1]
        dice[1] = tmp_dice[2]
        dice[2] = tmp_dice[3]
        dice[3] = tmp_dice[0]

class Solution:
    @staticmethod
    def solve(N: int, M: int, x: int, y: int, K: int,
              map_info: list[list[int]],
              move_info: list[int]):

        dx = [0, 0, 0, -1, 1]
        dy = [0, 1, -1, 0, 0]

        dice: list[int] = [0] * 6

        for direction in move_info:
            next_x = x + dx[direction]
            next_y = y + dy[direction]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            # direction 으로 주사위 회전
            rotate(direction, dice)

            # 지도, 주사위 바닥면 업데이트
            # print(next_x, next_y)
            if map_info[next_x][next_y] == 0:
                map_info[next_x][next_y] = dice[1]
            else:
                dice[1] = map_info[next_x][next_y]
                map_info[next_x][next_y] = 0

            # 주사위 상단면 출력
            print(dice[3])
            x = next_x
            y = next_y

if __name__ == "__main__":
    N: int
    M: int
    x: int
    y: int
    K: int
    map_info: list[list[int]]
    dice: list[int]
    N, M, x, y, K = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(N)]
    move_info = [int(x) for x in input().split()]
    Solution.solve(N, M, x, y, K, map_info, move_info)
