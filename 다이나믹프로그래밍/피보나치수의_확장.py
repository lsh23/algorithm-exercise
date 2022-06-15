from typing import List
class Solution:
    def DP(self, N:int) -> int:

        if N>0:
            print(1)

            dp: List[int] = [0] * (N + 1)
            dp[0] = 0
            dp[1] = 1

            for i in range(2, N + 1):
                dp[i] = (dp[i - 1] + dp[i - 2])%1000000000

            return dp[N]

        elif N<0:

            N = abs(N)
            dp: List[int] = [0] * (N + 2)
            dp[0] = 0
            dp[1] = 1
            dp[2] = -1
            # dp[1] = dp[0] + dp[-1]
            #  1    =  0        1

            # dp[0] = dp[-1] + dp[-2]
            #   0       1       -1

            # dp[-1] = dp[-2] + dp[-3]
            #   1       -1       2

            # dp[-2] = dp[-3] + dp[-4]
            #    -1      2       -3

            for i in range(1, N - 1):
                dp[i+2] = dp[i] - dp[i+1]
                if dp[i+2] > 0:
                    dp[i+2]%=1000000000
                else:
                    dp[i+2]%=-1000000000

            if dp[N]>0:
                print(1)
            elif dp[N]<0:
                print(-1)

            return abs(dp[N])

        else:
            print(0)
            return 0


if __name__ == '__main__':
    N :int = int(input())
    s :Solution = Solution()
    answer :int = s.DP(N)
    print(answer)