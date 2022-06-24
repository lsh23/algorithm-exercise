from typing import List
class Solution:
    def DP(self, T:int, W:int, falling_info:List[int] ) -> int:

        # k 초일때 위치가 p 이고 위치가 p 이고 이동 횟수가 w일 때  최대 갯수 dp[p][k][w]

        dp :List[List[List[int]]] = [[[0]*32 for _ in range(T+1)] for _ in range(3)]

        # if falling_info[1] == 1:
        #     dp[1][1][0]=1

        for i in range(1,T+1):
            for j in range(1,W+2):
                if falling_info[i] == 1:
                    dp[1][i][j] = max(dp[1][i-1][j]+1, dp[2][i-1][j-1]+1)
                    dp[2][i][j] = max(dp[1][i-1][j-1], dp[2][i-1][j])
                else:
                    if i == 1 and j == 1:
                        continue
                    dp[1][i][j] = max(dp[2][i-1][j-1], dp[1][i-1][j])
                    dp[2][i][j] = max(dp[1][i-1][j-1]+1, dp[2][i-1][j]+1)

        for i in range(W+2):
            answer = max(dp[1][T][i],dp[2][T][i])
        return answer


if __name__ == '__main__':
    T :int
    W :int
    T,W = map(int,input().split())
    falling_info :list[int] = [1]
    for _ in range(T):
        falling_info.append(int(input()))
    s :Solution = Solution()
    answer :int = s.DP(T,W, falling_info)
    print(answer)