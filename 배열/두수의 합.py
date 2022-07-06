import sys
from typing import List
class Solution:
    def solve(self, N:int, arr:List[int], x:int ) -> None:

        arr.sort()

        l:int = 0
        r:int = N-1

        answer: int = 0

        while l<r:
            sum = arr[l] + arr[r]
            if sum == x:
                answer += 1
                r -= 1
            elif sum > x:
                r -= 1
            else:
                l += 1

        return answer

if __name__ == '__main__':
    input = sys.stdin.readline

    N: int = int(input())
    arr: List[int] = [ int(x) for x in input().split() ]
    x: int = int(input())

    s :Solution = Solution()
    print(s.solve(N,arr,x))
