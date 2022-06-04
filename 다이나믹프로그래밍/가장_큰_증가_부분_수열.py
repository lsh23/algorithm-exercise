from typing import List
class Solution:
    def DP(self, N:int, numbers:List[int]) -> int:
        dp: List[int] = numbers[:]

        for i in range(1,N):
            for j in range(0,i+1):
                if numbers[i] > numbers[i-j]:
                    dp[i] = max(dp[i-j]+numbers[i],dp[i])

        return max(dp)


if __name__ == '__main__':
    N :int = int(input())
    numbers :List[int] = [ int(x) for x in input().split() ]
    # numbers = [ x for x in range(1,1001) ]
    s :Solution = Solution()
    answer :int = s.DP(N,numbers)
    print(answer)