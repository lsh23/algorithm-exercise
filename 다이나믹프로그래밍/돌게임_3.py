from typing import List
class Solution:
    def DP(self, N:int) -> str:

        dp: List[str] = [""] * (N+1)
        # dp[1] = "SK"
        # dp[2] = "CY"
        # dp[3] = "SK"
        # dp[4] = "SK"
        # dp[5] = "CY"
        # dp[6] = "SK"
        # dp[7] = "CY"
        # dp[8] = "SK

        dp[1] = "SK"
        dp[2] = "CY"
        dp[3] = "SK"
        dp[4] = "SK"

        for i in range(5,N+1):
            if all([dp[i-1]=="SK",dp[i-3]=="SK",dp[i-4]=="SK"]):
                dp[i]="CY"
            else:
                dp[i]="SK"

        return dp[N]
if __name__ == '__main__':
    N :int = int(input())
    s :Solution = Solution()
    answer :str = s.DP(N)
    print(answer)
