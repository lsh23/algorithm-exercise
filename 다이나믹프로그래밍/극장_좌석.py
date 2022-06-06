from typing import List
import sys
class Solution:
    def DP(self, N:int, M:int, vip_seat_number: List[int]) -> int:
        dp :List[int] = [0]*(N+1)

        dp[0]=1
        dp[1]=1
        dp[2]=2

        for i in range(3,N+1):
            dp[i] = dp[i-1] + dp[i-2]

        if M == 0:
            return dp[N]

        answer: int = 1

        cur = 0
        for seat_number in vip_seat_number:
            answer *= dp[seat_number-(cur+1)]
            cur = seat_number

        answer *= dp[N - cur]

        return answer


if __name__ == '__main__':
    input = sys.stdin.readline
    N: int = int(input())
    M: int = int(input())

    vip_seat_number = []
    for _ in range(M):
        seat_number = int(input())
        vip_seat_number.append(seat_number)

    s: Solution = Solution()
    answer: int = s.DP(N,M,vip_seat_number)
    print(answer)

