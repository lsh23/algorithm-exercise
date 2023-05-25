from fractions import Fraction


class Solution:
    @staticmethod
    def solve(n: int, target_roulette: list[str], cur_roulette: list[str]) -> int:

        if n == 1:
            print("1/1")
            return

        f: list[int] = [0] * len(cur_roulette)
        j: int = 0
        for i in range(1, len(cur_roulette)):
            while j > 0 and cur_roulette[i] != cur_roulette[j]:
                j = f[j - 1]
            if cur_roulette[i] == cur_roulette[j]:
                f[i] = j + 1
                j += 1

        target_roulette = target_roulette + target_roulette[:-1]
        j = 0
        cnt: int = 0
        for i in range(len(target_roulette)):
            while j > 0 and target_roulette[i] != cur_roulette[j]:
                j = f[j - 1]
            if target_roulette[i] == cur_roulette[j]:
                j += 1
            if j == len(cur_roulette):
                cnt += 1
                j = f[j - 1]

        if cnt != n:
            print(Fraction(cnt, n))
        else:
            print("1/1")


if __name__ == "__main__":
    N: int
    target_roulette: list[str]
    cur_roulette: list[str]
    N = int(input())
    target_roulette = input().split()
    cur_roulette = input().split()
    Solution.solve(N, target_roulette, cur_roulette)
