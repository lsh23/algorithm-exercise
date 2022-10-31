import sys
import heapq
from typing import List
class Solution:
    def solve(self, card_bundles:List[int] ) -> int:

        heapq.heapify(card_bundles)
        answer: int = 0

        while card_bundles and not len(card_bundles) == 1:
                sum = heapq.heappop(card_bundles) + heapq.heappop(card_bundles)
                answer += sum
                heapq.heappush(card_bundles, sum)

        return answer

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    card_bundles: List[int] = [ int(input()) for _ in range(N) ]
    s = Solution()
    print(s.solve(card_bundles))
