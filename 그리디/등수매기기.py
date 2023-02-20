import sys


class Solution:
    def solve(self, N:int, expected_ranks:list[int]) -> int:
        expected_ranks.sort()
        return sum([abs(i-x) for i,x in enumerate(expected_ranks, start=1)])


if __name__ == '__main__':
    input = sys.stdin.readline
    N: int = int(input())
    expected_ranks: list[int] = [int(input()) for _ in range(N)]
    s: Solution = Solution()
    print(s.solve(N, expected_ranks))