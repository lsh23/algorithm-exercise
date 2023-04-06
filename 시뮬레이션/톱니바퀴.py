def right_check(idx: int, clockwise: int, check: list[int]):
    if idx >= 3:
        return
    if gear_state[idx][2] != gear_state[idx + 1][6]:
        check[idx + 1] = clockwise * -1
        right_check(idx + 1, clockwise * -1, check)


def left_check(idx: int, clockwise: int, check: list[int]):
    if idx <= 0:
        return
    if gear_state[idx - 1][2] != gear_state[idx][6]:
        check[idx - 1] = clockwise * -1
        left_check(idx - 1, clockwise * -1, check)


class Solution:
    @staticmethod
    def solve(gear_state: list[str], K: int, rotate: list[tuple[int, int]]) -> int:
        for r in rotate:
            check: list[int] = [0] * 4

            r_gear = r[0] - 1
            clockwise = r[1]

            check[r_gear] = clockwise
            left_check(r_gear, clockwise, check)
            right_check(r_gear, clockwise, check)

            for i in range(4):
                if check[i] != 0:
                    if check[i] == 1:
                        gear_state[i] = gear_state[i][7] + gear_state[i][:7]
                    else:
                        gear_state[i] = gear_state[i][1:8] + gear_state[i][0]

        score: int = 0
        for i in range(4):
            if gear_state[i][0] == "1":
                score += 2 ** i
        return score


if __name__ == "__main__":
    gear_state: list[str]
    K: int
    rotate: list[tuple[int, int]]

    gear_state = [input() for _ in range(4)]
    K = int(input())
    rotate = [tuple(map(int, input().split())) for _ in range(K)]

    print(Solution.solve(gear_state, K, rotate))
