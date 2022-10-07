from typing import List
class Solution:
    def solve(self, N:int, graph:List[List[int]] ) -> None:

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if i==j:
                        graph[i][j]=0
                        continue
                    if graph[i][k] and graph[k][j] and graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]

        # print(graph)
        min_score: int = min([max(graph[i]) for i in range(N)])
        candidates: List[int] = [ i+1 for i in range(N) if max(graph[i])==min_score ]

        print(f'{min_score} {len(candidates)}')
        for c in candidates:
            print(c, end=' ')


if __name__ == '__main__':

    N: int = int(input())
    graph: List[List[int]] = [[50]*(N) for _ in range(N)]
    while True:
        i,j = map(int,input().split())
        if i == -1 and j == -1:
            break
        graph[i-1][j-1] = 1
        graph[j-1][i-1] = 1
    s :Solution = Solution()
    answer :int = s.solve(N,graph)
