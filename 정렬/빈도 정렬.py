import sys
from typing import List
class Number:
    def __init__(self, number:str, i:int):
        self.number = number
        self.first_index = i
        self.cnt = 1

    def add_count(self):
        self.cnt += 1

    def __gt__(self, other):
        if self.cnt > other.cnt:
            return True
        elif self.cnt < other.cnt:
            return False
        else:
            return self.first_index < other.first_index

    def __repr__(self):
        return " ".join([self.number for _ in range(self.cnt)])

class Solution:
    def solve(self, n: int, k:int, sequence: List[int]):

        h: dict[int,Number] = dict()
        l: List[Number] = []

        i:int = 0
        for s in sequence:
            if s in h:
                h[s].add_count()
            else:
                h[s]=Number(s,i)
                l.append(h[s])
            i+=1

        l.sort(reverse=True)

        for x in l:
            print(x, end=" ")

if __name__ == '__main__':
    input = sys.stdin.readline
    N,C = map(int,input().split())
    sequence = [ x for x in input().split() ]
    s :Solution = Solution()
    s.solve(N, C, sequence)