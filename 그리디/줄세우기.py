class Solution:
    def solve(self, n:int, children: list[int]) -> int:

        dp: list[int] = [0]*(n+1)
        for i in range(n):
            dp[children[i]] = dp[children[i]-1] + 1
        return n-max(dp)


if __name__ == "__main__":
    N: int = int(input())
    children = [int(x) for x in input().split()]
    s = Solution()
    print(s.solve(N, children))