import sys
import heapq
from typing import List

class Problem:
    def __init__(self, deadline: int, ramen: int):
        self.deadline = deadline
        self.ramen = ramen

    def __gt__(self, other):

        return self.deadline > other.deadline

    def __str__(self):
        return f'{self.deadline}, {self.ramen}'

    def __repr__(self):
        return f'{self.deadline}, {self.ramen}'

class Solution:
    def solve(self, problems: List[Problem]) -> int:

        heapq.heapify(problems)

        ramens: List[int] = []
        heapq.heapify(ramens)

        T: int = 1

        while problems:
                problem: Problem = heapq.heappop(problems)

                if problem.deadline >= T:
                    heapq.heappush(ramens,problem.ramen)
                    T+=1
                else:
                    if ramens[0] < problem.ramen:
                        heapq.heappop(ramens)
                        heapq.heappush(ramens, problem.ramen)

        return sum(ramens)

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    problems: List[Problem] = []
    for _ in range(N):
        deadline: int
        ramen: int
        deadline, ramen = map(int, input().split())
        problems.append(Problem(deadline,ramen))
    s = Solution()
    print(s.solve(problems))
