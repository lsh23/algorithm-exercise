class Solution:
    def DP(self, N:int) -> int:
        dp = [0]*(1000001)

        dp[1]=0

        for n in range(2,N+1):
            dp[n] = dp[n-1]+1
            if n % 3 == 0:
                dp[n] = min(dp[n],dp[n//3]+1)
            if n % 2 == 0:
                dp[n] = min(dp[n],dp[n//2]+1)

        return dp[N]

if __name__ == '__main__':
    N = int(input())
    s = Solution()
    answer = (s.DP(N))
    print(answer)