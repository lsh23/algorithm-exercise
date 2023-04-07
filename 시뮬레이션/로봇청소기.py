def rotate(d: int):
    return (d + 3) % 4


def bound(y: int, x: int, n: int, m: int) -> bool:
    return 0 <= y < n and 0 <= x < m


class Solution:
    @staticmethod
    def solve(n: int, m: int, r: int, c: int, d: int, room_info: list[list[int]]) -> int:

        ans: int = 0
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        cur_y, cur_x = r, c
        while True:

            # 1. 현재 칸 청소여부 확인 후, 청소 되어있지 않으면 청소
            if room_info[cur_y][cur_x] == 0:
                room_info[cur_y][cur_x] = 2
                ans += 1

            around_all_cleaned: bool = True
            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                if not bound(next_y, next_x, n, m):
                    continue
                if room_info[next_y][next_x] == 0:
                    around_all_cleaned = False
                    break
            # 2. 현재 칸 주변 4칸 중 청소되지 않은 빈칸이 없는 경우,
            if around_all_cleaned:
                # 현재 방향을 유지한 채로 한칸 후진 할 수 있으면 후진
                #                       후진 할 수 없으면 작동 중지
                next_y = cur_y + dy[d] * -1
                next_x = cur_x + dx[d] * -1
                if not bound(next_y, next_x, n, m):
                    break
                if room_info[next_y][next_x] == 1:
                    break
                cur_y, cur_x = next_y, next_x
            else:
                # 3. 현재 칸 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
                # 반시계로 90 회전
                d = rotate(d)
                next_y = cur_y + dy[d]
                next_x = cur_x + dx[d]
                # 회전 후 방향 기준으로 앞쪽 칸이 청소되지 않은 빈칸인 경우 한칸 전진
                if bound(next_y, next_x, n, m):
                    if room_info[next_y][next_x] == 0:
                        cur_y, cur_x = next_y, next_x

        # for r in room_info:
        #     print(r)

        return ans


if __name__ == "__main__":
    N: int
    M: int
    r: int
    c: int
    d: int
    room_info: list[list[int]]

    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    room_info = [[int(x) for x in input().split()] for _ in range(N)]

    print(Solution.solve(N, M, r, c, d, room_info))
