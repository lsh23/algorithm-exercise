from typing import List
class Solution:
    def DP(self, N:int) -> int:

        dp: List[int] = [0]*(N+5)

        dp[1] = 3
        dp[2] = 7
        for i in range(3,N+1):
                dp[i] = (2 * dp[i-1] + dp[i-2]) % 9901

        return dp[N]

    def DP2(self, N:int) -> int:

        dp: List[List[int]] = [[0]*3for _ in range(N+5)]

        dp[1][0] = 1
        dp[1][1] = 1
        dp[1][2] = 1

        for i in range(2,N+1):
            dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
            dp[i][1] = dp[i-1][0] + dp[i-1][2]
            dp[i][2] = dp[i-1][0] + dp[i-1][1]

        return dp[N][0] + dp[N][1] + dp[N][2]


if __name__ == '__main__':
    N: int = int(input())
    s = Solution()
    answer = s.DP(N)
    # answer = s.DP2(N)
    print(answer)