import sys
import heapq


class Solution:
    def solve(self, N:int, commands:list[int] ) -> None:

        heap: list[int] = []

        for command in commands:
            if command == 0:
                if heap:
                    print(-1*heapq.heappop(heap))
                else:
                    print(0)
            else:
                heapq.heappush(heap, -1*command)


if __name__ == '__main__':
    input = sys.stdin.readline
    N: int = int(input())
    commands: list[int] = [ int(input()) for _ in range(N)]
    s = Solution()
    s.solve(N,commands)



