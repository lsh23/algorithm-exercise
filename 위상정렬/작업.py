import sys
from typing import List
from collections import deque
class Solution:
    def solve(self, N: int, job_info: List[List[int]]) -> int:

        job_time: List[int] = [0]*(N+1)
        indegree: List[int] = [0]*(N+1)
        graph: List[List[int]] = [ [0]*(N+1) for _ in range(N+1) ]
        q:deque = deque()
        i: int = 1
        for job in job_info:
            time: int = job[0]
            job_time[i] = time
            if len(job) == 2:
                q.append(i)
            else:
                for j in job[2:]:
                    graph[j][i] = 1
                    indegree[i]+=1
            i+=1


        # for i in range(1,N+1):
        #     for j in range(1,N+1):
        #         print(graph[i][j], end=" ")
        #     print()


        while q:
            job_i: int = q.popleft()
            max_time: int = 0
            for j in range(1, N+1):
                if graph[job_i][j]:
                    indegree[j]-=1
                    if indegree[j] == 0:
                        q.append(j)
                if graph[j][job_i]:
                    max_time = max(max_time,job_time[j])
            job_time[job_i]+=max_time

        return job_time[N]


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    job_info = [ [int(x) for x in input().split()] for _ in range(N) ]
    s :Solution = Solution()
    answer :int = s.solve(N, job_info)
    print(answer)