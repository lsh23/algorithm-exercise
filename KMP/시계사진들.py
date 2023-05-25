class Solution:
    @staticmethod
    def solve(n: int, clock_1: list[int], clock_2: list[int]) -> int:
        clock_1_all: list[int] = [0] * 360_000
        clock_2_all: list[int] = [0] * 360_000

        for x in clock_1:
            clock_1_all[x] = 1
        for x in clock_2:
            clock_2_all[x] = 1

        clock_2.sort()
        clock_2_start = clock_2[0]
        clock_2_end = clock_2[n - 1]

        f: list[int] = [0] * (clock_2_end - clock_2_start + 1)
        j: int = 0

        clock_2_all = clock_2_all[clock_2_start:clock_2_end + 1]

        for i in range(1, len(f)):
            while j > 0 and clock_2_all[i] != clock_2_all[j]:
                j = f[j - 1]
            if clock_2_all[i] == clock_2_all[j]:
                f[i] = j + 1
                j += 1

        clock_1_all = clock_1_all + clock_1_all
        j = 0
        for i in range(0, len(clock_1_all)):
            while j > 0 and clock_1_all[i] != clock_2_all[j]:
                j = f[j - 1]
            if clock_1_all[i] == clock_2_all[j]:
                j += 1
            if j == len(clock_2_all):
                return "possible"

        return "impossible"


if __name__ == "__main__":
    n: int
    clock_1 = list[int]
    clock_2 = list[int]
    n = int(input())
    clock_1 = [int(x) for x in input().split()]
    clock_2 = [int(x) for x in input().split()]
    print(Solution.solve(n, clock_1, clock_2))
