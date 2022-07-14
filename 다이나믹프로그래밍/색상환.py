from typing import List
import sys
class Solution:
    def DP(self, N:int, K:int) -> int:

        dp: List[List[int]] = [ [0]*(K+1) for _ in range(N+5)]

        for i in range(N+1):
            dp[i][0] = 1

        dp[1][1]=1

        for i in range(2,N+1):
            for j in range(1,K+1):
                if j*2 <= i+1:
                    dp[i][j] = (dp[i-2][j-1] + dp[i-1][j])%1000000003

        # for i in range(N+1):
        #     print(dp[i])

        return (dp[N-3][K-1] + dp[N-1][K])%1000000003



if __name__ == '__main__':
    N: int = int(input())
    K: int = int(input())
    s = Solution()
    answer = s.DP(N,K)
    print(answer)