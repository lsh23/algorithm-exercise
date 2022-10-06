from typing import List
class Solution:
    def solve(self, N:int, graph:List[List[int]] ) -> None:

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = 1

        for i in range(N):
            for j in range(N):
                print(graph[i][j], end=" ")
            print()

if __name__ == '__main__':

    N: int = int(input())
    graph: List[List[int]] = [ [ int(x) for x in input().split() ] for _ in range(N) ]
    s :Solution = Solution()
    answer :int = s.solve(N,graph)
