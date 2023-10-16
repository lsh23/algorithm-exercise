import heapq


class Solution:
    @staticmethod
    def solve(n: int, M: int, in_count: list[int], dependency: list[list[int]]):
        q = []
        for i in range(1, n + 1):
            q.append((in_count[i], i))

        solved = [0] * (n + 1)
        heapq.heapify(q)

        answer = []
        while q:
            in_cnt, problem = heapq.heappop(q)
            if solved[problem] != 0:
                continue
            if in_cnt != 0:
                heapq.heappush(q, (in_cnt, problem))
                continue
            solved[problem] = 1
            for d in dependency[problem]:
                in_count[d] -= 1
                heapq.heappush(q, (in_count[d], d))
            answer.append(problem)

        print(*answer)


if __name__ == "__main__":
    N: int
    M: int
    N, M = map(int, input().split())
    in_count = [0] * (N + 1)
    dependency = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        in_count[B] += 1
        dependency[A].append(B)

    Solution.solve(N, M, in_count, dependency)
