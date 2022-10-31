import sys
import heapq
from typing import List
# class Solution:
#     def solve(self, N:int, tables:List[int] ) -> int:
#         return -1*heapq.nsmallest(N,tables)[-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    tables: List[int] = []
    for _ in range(N):
        tables += [ -int(x) for x in input().split() ]
        tables = heapq.nsmallest(N, tables)

    # s = Solution()
    print(-1*tables[-1])
