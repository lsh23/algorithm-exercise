import sys
from typing import List
class Solution:
    def solve(self, N:int, stocks:List[int] ) -> int:

        answer: int = 0

        future_stock: int = stocks[N-1]
        for i in range(N-2,-1,-1):
            if future_stock > stocks[i]:
                answer += future_stock - stocks[i]
            else:
                future_stock = stocks[i]

        return answer



if __name__ == '__main__':
    input = sys.stdin.readline
    T:int = int(input())
    for _ in range(T):
        N: int = int(input())
        stocks = [ int(x) for x in input().split() ]
        s :Solution = Solution()
        answer :int = s.solve(N, stocks)
        print(answer)