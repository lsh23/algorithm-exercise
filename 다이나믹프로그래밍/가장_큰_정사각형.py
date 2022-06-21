from typing import List
class Solution:
    def DP(self, N:int, M:int, arr: List[List[int]]) -> int:

        dp: List[List[int]] = [ [0]*M for _ in range(N) ]

        max_l: int = 0
        for i in range(N):
            for j in range(M):
                if i==0 or j==0:
                    dp[i][j]=arr[i][j]
                elif arr[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                max_l = max(max_l,dp[i][j])

        return max_l*max_l


if __name__ == '__main__':
    N: int
    M: int
    N,M = map(int,input().split())
    arr: List[List[int]] = [ [int(x) for x in input()] for _ in range(N) ]
    s :Solution = Solution()
    answer :int = s.DP(N,M,arr)
    print(answer)