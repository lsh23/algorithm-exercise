from typing import List

class Solution:
    def DP(self, S1:str, S2:str) -> int:

        n1 = len(S1)
        n2 = len(S2)
        dp: List[int] = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if S1[i-1]==S2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        answer = max([max(row) for row in dp])
        return answer



if __name__ == '__main__':
    S1: str = input()
    S2: str = input()
    s :Solution = Solution()
    answer :int = s.DP(S1,S2)
    print(answer)