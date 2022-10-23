import sys
import heapq
from typing import List
class Solution:
    def solve(self, N:int, commands:List[int] ) -> int:

        heap: List[int] = []

        for command in commands:
            if command == 0:
                if heap:
                    print(heapq.heappop(heap)[1])
                else:
                    print(0)
            else:
                heapq.heappush(heap, (abs(command), command))


if __name__ == '__main__':
    input = sys.stdin.readline
    N: int = int(input())
    commands: List[int] = [ int(input()) for _ in range(N)]
    s = Solution()
    s.solve(N,commands)



