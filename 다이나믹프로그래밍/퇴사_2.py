from typing import List, Tuple
import sys

class Solution:
    def DP(self, N:int, t_p_list:List[Tuple[int,int]]) -> int:
        dp: List[int] = [0] * (N+2)

        # dp[n] -> n일 까지 일했을 떄의 최대 보수 값

        for i in range(1,N+1):
            t_i :int = t_p_list[i][0]
            p_i :int = t_p_list[i][1]
            dp[i + 1] = max(dp[i], dp[i + 1])
            if i+t_i > N+1:
                continue
            dp[i+t_i] = max(dp[i+t_i], dp[i]+p_i)

        return dp[N+1]



if __name__ == '__main__':
    N :int = int(input())
    t_p_list :List[Tuple[int,int]] = [ (0,0) ]
    for _ in range(N):
        t,p = map(int,sys.stdin.readline().split())
        t_p_list.append((t,p))

    s :Solution = Solution()
    answer :int = s.DP(N,t_p_list)
    print(answer)