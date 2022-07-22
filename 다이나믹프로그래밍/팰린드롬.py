import sys
from typing import List

class Solution:
    def DP(self, N:int, arr:List[int]) -> List[List[int]]:

        dp: List[List[int]] = [[0]*(N+1) for _ in range(N+1)]

        arr.insert(0,0)

        for i in range(1,N+1):
            dp[i][i]=1
            if arr[i] == arr[i-1]:
                dp[i-1][i]=1

        for i in range(2,N+1):
            for j in range(1,N+1-i):
                if dp[j+1][j+i-1] and arr[j] == arr[j+i]:
                    dp[j][j+i] = 1

        return dp

if __name__ == '__main__':
    input = sys.stdin.readline
    N :int = int(input())
    arr = [ int(x) for x in input().split() ]
    M :int = int(input())
    s :Solution = Solution()
    sol :List[int] = s.DP(N,arr)
    s: int
    m: int
    for i in range(M):
        s,e = map(int,input().split())
        print(sol[s][e])
