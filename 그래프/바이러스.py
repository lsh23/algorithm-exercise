from collections import deque


class Solution:
    def solve(self, N: int, graph: list[list[int]]):
        cnt: int = -1

        visited: list[int] = [0]*(N+1)
        visited[1] = 1

        q: deque[int] = deque()
        q.append(1)

        while q:
            cur = q.popleft()
            cnt += 1
            for k in graph[cur]:
                if visited[k] == 0:
                    q.append(k)
                    visited[k] = 1

        return cnt


if __name__ == '__main__':
    N: int = int(input())
    M: int = int(input())
    graph: list[list[int]] = [ [] for _ in range(N+1) ]
    for _ in range(M):
        i: int
        j: int
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    s: Solution = Solution()
    print(s.solve(N, graph))