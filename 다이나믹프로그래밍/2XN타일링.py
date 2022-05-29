from typing import List
class Solution:
    def DP(self, N:int) -> int:

        dp = [0]*(N+1)

        dp[1] = 1
        dp[2] = 2

        for k in range(3,N+1):
            dp[k] = dp[k-1] + dp[k-2]

        return dp[N]

if __name__ == '__main__':
    N = int(input())

    s = Solution()
    answer = (s.DP(N))
    print(answer)

