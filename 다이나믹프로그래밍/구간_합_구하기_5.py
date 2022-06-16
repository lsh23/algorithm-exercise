from typing import List
import sys
class Solution:
    def DP(self, N:int, numbers:List[int]) -> List[List[int]]:
        dp: List[List[int]] = [[0]*(N+1) for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,N+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + numbers[i][j]
        return dp

if __name__ == '__main__':
    input = sys.stdin.readline
    N,M = map(int,input().split())

    numbers = [ [0]*(N+1) ]
    for _ in range(N):
        numbers.append([0] + [ int(x) for x in input().split() ])

    s: Solution = Solution()
    dp: List[List[int]]= s.DP(N,numbers)

    for _ in range(M):
        x1,y1,x2,y2 = map(int, input().split())
        print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])