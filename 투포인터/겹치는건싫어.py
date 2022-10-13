import sys
from typing import List
class Solution:
    def solve(self, n: int, k:int, sequence: List[int]) -> int:
        p_1: int = 0
        p_2: int = 0

        cnts: List = [0]*100001
        answer: int = 1

        while p_1 <= p_2 and p_2 < n:
            if cnts[sequence[p_2]] != k:
                cnts[sequence[p_2]] += 1
                p_2 += 1
            else:
                cnts[sequence[p_1]]-=1
                p_1 += 1
            answer = max(answer, p_2-p_1)

        return answer


if __name__ == '__main__':
    input = sys.stdin.readline
    N,K = map(int,input().split())
    sequence = [ int(x) for x in input().split() ]
    s :Solution = Solution()
    answer :int = s.solve(N, K, sequence)
    print(answer)