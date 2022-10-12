import sys
import heapq
from typing import List

class Solution:
    def solve(self, inputs:List[int] ) -> None:
        pq = []

        for i in inputs:
            if i == 0:
                if pq:
                    print(heapq.heappop(pq))
                else:
                    print(0)
            else:
                heapq.heappush(pq, i)

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    inputs: List[int] = [ int(input()) for _ in range(N)]
    s = Solution()
    s.solve(inputs)


