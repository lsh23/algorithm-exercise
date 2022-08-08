from typing import List
class Solution:
    def DP(self, N:int, M:int, fixed_seats:List[int]) -> int:
        dp: List[int] = [0]*(N+1)

        dp[0] = 1
        dp[1] = 1


        for i in range(2,N+1):
            if i in fixed_seats or i-1 in fixed_seats:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i - 1] + dp[i-2]

        return dp[N]

if __name__ == '__main__':
    N: int = int(input())
    M: int = int(input())
    fixed_seats: List[int] = []
    for _ in range(M):
        fixed_seats.append(int(input()))
    s = Solution()
    print(s.DP(N,M,fixed_seats))