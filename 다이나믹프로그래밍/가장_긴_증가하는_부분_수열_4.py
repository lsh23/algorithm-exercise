from typing import List
class Solution:
    def DP(self, N:int, numbers:List[int]) -> int:
        dp: List[int] = [1] * N

        for i in range(N):
            for j in range(i):
                if numbers[i] > numbers[j]:
                    dp[i] = max(dp[i], dp[j]+1)


        max_length: int = max(dp)
        print(max_length)

        max_idx: int = dp.index(max_length)
        lis: List[int] = []

        while max_idx >=0:
            if dp[max_idx] == max_length:
                lis.append(numbers[max_idx])
                max_length-=1
            max_idx-=1

        while lis:
            print(lis.pop(),end=" ")

if __name__ == '__main__':
    N :int = int(input())
    numbers :List[int] = [ int(x) for x in input().split() ]
    s :Solution = Solution()
    answer :int = s.DP(N,numbers)