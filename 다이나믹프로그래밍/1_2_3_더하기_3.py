from typing import List
import sys
class Solution:
    def DP(self) -> List[int]:

        dp: List[int] = [0] * 1000001
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, 1000001):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009

        return dp

if __name__ == '__main__':
    T :int = int(input())
    s = Solution()
    answer = (s.DP())
    for _ in range(T):
        n :int = int(sys.stdin.readline())
        print(answer[n])
