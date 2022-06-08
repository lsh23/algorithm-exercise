from typing import List
class Solution:
    def DP(self, N:int) -> None:
        dp: List[int]= [0]*(N+1)
        pre: List[int] = [0]*(N+1)
        dp[1]=0
        pre[1]=0
        pre[2]=1
        pre[3]=1

        for n in range(2,N+1):
            dp[n] = dp[n-1]+1
            pre[n] = n-1
            if n % 3 == 0:
                if dp[n] >= dp[n//3]+1:
                    dp[n] = dp[n//3]+1
                    pre[n] = n//3
                # dp[n] = min(dp[n],dp[n//3]+1)
            if n % 2 == 0:
                # dp[n] = min(dp[n],dp[n//2]+1)
                if dp[n] >= dp[n//2]+1:
                    dp[n] = dp[n//2]+1
                    pre[n] = n//2

        print(dp[N])
        k = N
        while k>=1:
            print(k, end=" ")
            k=pre[k]


if __name__ == '__main__':
    N = int(input())
    s = Solution()
    s.DP(N)