from typing import List
import sys
class Solution:
    def DP(self, N:int, M:int, coins:List[int]) -> int:
        dp : List[int] = [0]*(M+1)

        dp[0]=1
        for i in range(len(coins)):
            for j in range(coins[i],M+1):
                dp[j] += dp[j-coins[i]]

        return dp[M]

if __name__ == '__main__':
    input = sys.stdin.readline
    T: int = int(input())
    for _ in range(T):
        N :int = int(input())
        coins = [int(x) for x in input().split()]
        M :int = int(input())
        s :Solution = Solution()
        answer :int = s.DP(N,M,coins)
        print(answer)