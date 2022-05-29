from typing import List
class Solution:
    def DP(self, N:int, costs: List[List[int]]) -> int:

        dp = [[0]*N for i in range(N)]

        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for i in range(1,N):
            dp[i][0] = min(dp[i-1][1]+costs[i][0], dp[i-1][2]+costs[i][0])
            dp[i][1] = min(dp[i-1][0]+costs[i][1], dp[i-1][2]+costs[i][1])
            dp[i][2] = min(dp[i-1][0]+costs[i][2], dp[i-1][1]+costs[i][2])


        return min(dp[N-1][0],dp[N-1][1],dp[N-1][2])

if __name__ == '__main__':
    N = int(input())

    costs = [ list(map(int,input().split())) for _ in range(N)]

    s = Solution()
    answer = (s.DP(N, costs))
    print(answer)

