class Solution:
    def DP(self, n:int) -> int:
        dp = [0]*(12)

        dp[1]=1
        dp[2]=2
        dp[3]=4

        for k in range(4,n+1):
            dp[k] = dp[k-1]+dp[k-2]+dp[k-3]

        return dp[n]

if __name__ == '__main__':
    N = int(input())
    s = Solution()
    for _ in range(N):
        n = int(input())
        answer = (s.DP(n))
        print(answer)