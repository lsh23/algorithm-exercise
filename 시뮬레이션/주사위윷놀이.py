class Solution:
    @staticmethod
    def solve(dices: list[int]) -> int:
        max_point: int = 0
        order: list[int] = [0] * 10

        scores: list[int] = \
            [0, 2, 4, 6, 8, 10,
             12, 14, 16, 18, 20,
             22, 24, 26, 28, 30,
             32, 34, 36, 38, 40,
             13, 16, 19,
             22, 24,
             28, 27, 26,
             25, 30, 35, 41]

        next: dict[int, int] = {}

        next[5] = [0, 21, 22, 23, 29, 30]
        next[21] = [0, 22, 23, 29, 30, 31]
        next[22] = [0, 23, 29, 30, 31, 20]
        next[23] = [0, 29, 30, 31, 20, 32]

        next[10] = [0, 24, 25, 29, 30, 31]
        next[24] = [0, 25, 29, 30, 31, 20]
        next[25] = [0, 29, 30, 31, 20, 32]

        next[15] = [0, 26, 27, 28, 29, 30]
        next[26] = [0, 27, 28, 29, 30, 31]
        next[27] = [0, 28, 29, 30, 31, 20]
        next[28] = [0, 29, 30, 31, 20, 32]

        next[29] = [0, 30, 31, 20, 32, 32]
        next[30] = [0, 31, 20, 32, 32, 32]
        next[31] = [0, 20, 32, 32, 32, 32]

        next[16] = [0, 17, 18, 19, 20, 32]
        next[17] = [0, 18, 19, 20, 32, 32]
        next[18] = [0, 19, 20, 32, 32, 32]
        next[19] = [0, 20, 32, 32, 32, 32]
        next[20] = [0, 32, 32, 32, 32, 32]

        def get_next_location(cur_location: int, dice: int) -> int:

            if cur_location in next:
                return next[cur_location][dice]

            if cur_location + dice >= 32:
                return 32

            return cur_location + dice

        def play(order: list[int]):
            point: int = 0
            horse_location: list[int] = [0] * 4
            board: list[int] = [0] * 51

            for i in range(10):
                horse = order[i]
                dice = dices[i]
                cur_location = horse_location[horse]

                if cur_location == 32:  # 이미 완료된 말을 움직이려고 하는 경우도 중단
                    return 0

                next_location = get_next_location(cur_location, dice)

                if next_location != 32 and board[next_location] != 0:  # 이동할 칸에 다른 말이 있으면 중단
                    return 0

                horse_location[horse] = next_location
                board[cur_location] = 0
                board[next_location] = 1

                if next_location != 32:  # 도착하면 추가되는 점수는 없음
                    point += scores[next_location]

            return point

        def dfs(l):
            nonlocal max_point
            if l == 10:
                max_point = max(play(order), max_point)
                return
            for i in range(4):
                order[l] = i
                dfs(l + 1)

        dfs(0)

        return max_point


if __name__ == "__main__":
    dices: list[int] = [int(x) for x in input().split()]
    print(Solution.solve(dices))
