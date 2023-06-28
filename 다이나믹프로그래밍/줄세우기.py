class Solution:
    @staticmethod
    def solve(n: int, height: list[int]) -> int:
        dp: list[int] = [1] * n

        for i in range(n):
            for j in range(i):
                if height[i] > height[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return n - max(dp)


if __name__ == "__main__":
    N: int
    heights: list[int]
    N = int(input())
    heights = [int(input()) for _ in range(N)]
    print(Solution.solve(N, heights))
