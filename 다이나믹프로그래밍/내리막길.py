import sys
from typing import List
sys.setrecursionlimit(200000)
class Solution:
    def DP(self, M:int, N:int,  map_info: List[List[int]]) -> int:

        dp: List[List[int]] = [[-1] * N for _ in range(M)]

        dy = [0, 1, -1, 0]
        dx = [1, 0, 0, -1]

        def dfs(y:int, x:int):
            if y==M-1 and x==N-1:
                return 1
            else:
                if dp[y][x] != -1:
                    return dp[y][x]
                dp[y][x]=0
                for i in range(4):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if next_y < 0 or next_y >= M or next_x < 0 or next_x >= N:
                        continue
                    if map_info[y][x] <= map_info[next_y][next_x]:
                        continue
                    dp[y][x]+=dfs(next_y,next_x)
                return dp[y][x]



        dfs(0,0)

        # for i in range(M):
        #     print(dp[i])

        return max([max(x) for x in dp])



if __name__ == '__main__':
    M: int
    N: int
    M,N = map(int,input().split())
    map_info: List[List[int]]
    map_info = [[int(x) for x in input().split()] for _ in range(M)]
    s :Solution = Solution()
    answer :int = s.DP(M,N,map_info)
    a :str

    print(answer)
    b : List[int]
