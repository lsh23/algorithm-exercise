import sys
from typing import List,Tuple
import heapq
class Solution:
    def solve(self, N:int, L:int, arr:List[int] ) -> None:

        pq: List[Tuple[int,int]] = []

        # D(0) = A(0)
        # D(1) = min(A(0),A(1))
        # D(2) = min(A(0),A(1),A(2))
        # D(3) = min(A(1),A(2),A(3))
        # D(4) = min(A(2),A(3),A(4))

        for i in range(N):
            heapq.heappush(pq,(arr[i],i))
            top_index: int = pq[0][1]
            while top_index < i-L+1:
                heapq.heappop(pq)
                top_index = pq[0][1]

            print(pq[0][0],end=" ")

if __name__ == '__main__':
    input = sys.stdin.readline

    N:int
    L:int
    N,L = map(int,input().split())

    arr = [ int(x) for x in input().split() ]

    s :Solution = Solution()
    s.solve(N,L,arr)
