from typing import List, Tuple
class Solution:
    def DP(self, N:int) -> int:

        # 1 or 00

        # DP[1] = 1  # 1

        # DP[2] = 2  # 00 11

        # DP[3] = 3  # 001 100 111

        # DP[N] = DP[N-1] + DP[N-1]

        dp: List[int] = [0]*(N+3)
        dp[1]=1
        dp[2]=2

        for i in range(3,N+1):
            dp[i] = (dp[i-1] + dp[i-2])%15746

        return dp[N]


if __name__ == '__main__':
    N :int = int(input())
    s :Solution = Solution()
    answer :int = s.DP(N)
    print(answer)