import sys
from typing import List, Tuple
class Solution:
    def DP(self, N:int, graph: List[List[int]]) -> int:

        dp: List[List[int]] = [[1000000]*3 for _ in range(N)]
        dp[0][1] = graph[0][1]
        dp[0][2] = dp[0][1] + graph[0][2]

        for i in range(1,N):
            for j in range(3):
                if i==0 and j==0:
                    continue
                if j==0:
                    dp[i][j] = min(dp[i-1][j]+graph[i][j], dp[i-1][j+1]+graph[i][j])
                if j==1:
                    dp[i][j] = min(dp[i][j-1]+graph[i][j],dp[i-1][j-1]+graph[i][j], dp[i-1][j]+graph[i][j],dp[i-1][j+1]+graph[i][j])
                if j==2:
                    dp[i][j] = min(dp[i][j-1]+graph[i][j],dp[i-1][j-1]+graph[i][j], dp[i-1][j]+graph[i][j])

        return dp[N-1][1]

if __name__ == '__main__':
    input = sys.stdin.readline

    k = 1
    while True:
        N :int = int(input())
        if N == 0:
            break
        graph: List[List[int]] = []
        for _ in range(N):
            graph.append([int(x) for x in input().split()])
        # print(graph)
        s :Solution = Solution()
        answer :int = s.DP(N, graph)
        print("%d. %d" % (k,answer))
        k+=1