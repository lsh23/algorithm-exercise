import sys
from typing import List
from collections import deque


class Solution:
    def solve(self, N: int, job_info: List[List[int]]) -> int:

        job_time: List[int] = [0] * (N + 1)
        indegree: List[int] = [0] * (N + 1)
        graph: List[List[int]] = [[] for _ in range(N + 1)]
        q: deque = deque()
        i: int = 1
        for job in job_info:
            time: int = job[0]
            job_time[i] = time
            for j in job[2:]:
                graph[j].append(i)
                indegree[i] += 1
            i += 1

        total_job_time: List[int] = [0] * (N + 1)

        for i in range(1, N + 1):
            if indegree[i] == 0:
                q.append(i)
                total_job_time[i] = job_time[i]

        while q:
            job_i: int = q.popleft()
            for j in graph[job_i]:
                indegree[j] -= 1
                total_job_time[j] = max(total_job_time[j], total_job_time[job_i])
                if indegree[j] == 0:
                    q.append(j)
                    total_job_time[j] = total_job_time[j] + job_time[j]

        return max(total_job_time[1:])


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    job_info = [[int(x) for x in input().split()] for _ in range(N)]
    s: Solution = Solution()
    answer: int = s.solve(N, job_info)
    print(answer)