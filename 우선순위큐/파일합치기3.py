import sys
import heapq
from typing import List
class Solution:
    def solve(self, chapters:List[int] ) -> int:

        heapq.heapify(chapters)
        answer: int = 0

        while len(chapters) > 1:
                sum = heapq.heappop(chapters) + heapq.heappop(chapters)
                answer += sum
                heapq.heappush(chapters, sum)

        return answer

if __name__ == '__main__':
    input = sys.stdin.readline
    T:int = int(input())
    for _ in range(T):
        K: int = int(input())
        chapters: List[int] = [ int(x) for x in input().split() ]
        s = Solution()
        print(s.solve(chapters))
