import sys
from typing import List
class Solution:
    def solve(self, n: int, m:int, sequence: List[int]) -> int:

        sequence.sort()

        p_1:int = 0
        p_2:int = 1

        diff: int = 2000000001

        while p_1 < p_2 and p_2 < n:
            if sequence[p_2] - sequence[p_1] < m:
                p_2 += 1
            else:
                if diff >= sequence[p_2] - sequence[p_1]:
                    diff = sequence[p_2] - sequence[p_1]
                p_1 += 1
                if p_1 == p_2:
                    p_2+=1

        return diff



if __name__ == '__main__':
    input = sys.stdin.readline
    N,M = map(int,input().split())
    sequence = [ int(input()) for _ in range(N)]
    s :Solution = Solution()
    answer :int = s.solve(N, M, sequence)
    print(answer)