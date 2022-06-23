from typing import List
class Solution:
    def DP(self, pw:str) -> int:

        n:int = len(pw)
        dp: List[int] = [0]*(n+1)

        dp[0]=1

        pw = '0'+pw

        for i in range(1,n+1):
            if 1<= int(pw[i]) <=9:
                dp[i] = (dp[i] + dp[i-1])%1000000

            if 10<= int(pw[i-1:i+1]) <= 26:
                dp[i] = (dp[i] + dp[i-2])%1000000

        return dp[n]



if __name__ == '__main__':
    pw: str = input()
    s :Solution = Solution()
    answer :int = s.DP(pw)
    print(answer)