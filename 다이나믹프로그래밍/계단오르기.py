from typing import List
class Solution:
    def DP(self, N:int, stairs: List) -> int:
        dp = [[0]*(301) for _ in range(3)]
        dp[1][1] = stairs[1]

        for k in range(2,N+1):
            dp[1][k] = max(dp[2][k-2],dp[1][k-2])+stairs[k]
            dp[2][k] = dp[1][k-1] + stairs[k]

        return max(dp[1][N],dp[2][N])

    def DP2(self, N:int, stairs: List) -> int:
        dp = [0] * (301)
        # i번째 계단까지 올라섰을 때 밟지 않을 계단의 합의 최솟값, i번째 계단은 반드시 밟지 않음
        dp[1] = stairs[1]
        dp[2] = stairs[2]
        dp[3] = stairs[3]

        for k in range(N+1):
            dp[k] = min(dp[k-2],dp[k-3]) + stairs[k]

        return sum(stairs)-min(dp[k-1],dp[k-2])

    def DFS(self, N:int, stairs: List) -> int:
        global max_score
        max_score = 0
        def dfs(k:int, score:int, consequence:int):
            global max_score
            # print(k,score,consequence)
            if k==N:
                max_score = max(max_score, score)
            else:
                if k+1 <= N and consequence+1 < 3:
                        dfs(k+1, score+stairs[k+1], consequence+1)
                if k+2 <= N:
                    dfs(k+2, score+stairs[k+2], 1)
        dfs(0,0,0)
        return max_score

if __name__ == '__main__':
    N = int(input())
    s = Solution()
    stairs = [ int(input()) for _ in range(N) ]
    assert len(stairs) == N
    stairs.insert(0,0)

    # answer = s.DP(N, stairs)
    answer = s.DP2(N,stairs)
    # answer = s.DFS(N,stairs)
    print(answer)