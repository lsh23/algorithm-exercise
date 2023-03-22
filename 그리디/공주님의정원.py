import sys


class Solution:
    def solve(self, n: int, flowers: list[tuple[int, int, int, int]]) -> int:
        ans: int = 0

        # for f in flowers:
        #     print(f)

        prev_wither_month: int = 3
        prev_wither_day: int = 1

        i: int = 0
        while i < n:

            if prev_wither_month >= 12:
                break

            max_wither_month: int = 0
            max_wither_day: int = 0

            for j in range(i, n):
                j_blossom_month, j_blossom_day, j_wither_month, j_wither_day = flowers[j]
                if prev_wither_month > j_blossom_month or (
                        prev_wither_month == j_blossom_month and prev_wither_day >= j_blossom_day):

                    if max_wither_month < j_wither_month or (
                            max_wither_month == j_wither_month and max_wither_day < j_wither_day):
                        max_wither_month = j_wither_month
                        max_wither_day = j_wither_day
                else:
                    break
                i += 1

            if max_wither_month == 0 and max_wither_day == 0:   # 매일 꽃이 한가지 이상 피어 있지 못한 경우
                break

            prev_wither_month = max_wither_month
            prev_wither_day = max_wither_day
            # print(max_wither_month, max_wither_day)

            ans += 1

        if prev_wither_month < 12:
            ans = 0

        return ans


if __name__ == '__main__':
    input = sys.stdin.readline
    N: int = int(input())
    flowers: list[tuple[int, int, int, int]] = [tuple(map(int, input().strip().split())) for _ in range(N)]
    flowers.sort()
    s: Solution = Solution()
    print(s.solve(N, flowers))
