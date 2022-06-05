from typing import List, Tuple
class Solution:
    def DP(self, N:int) -> int:

        dp: List[int] = [0] * (N+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2,N+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[N]

if __name__ == '__main__':
    N :int = int(input())
    s :Solution = Solution()
    answer :int = s.DP(N)
    print(answer)