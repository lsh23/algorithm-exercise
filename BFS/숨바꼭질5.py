from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, k: int) -> int:
        # 수빈이는 x-1, x+1 x*2 이동
        # 동생은 가속하면서 이동

        ans: int = -1
        visited: list[int] = [[-1] * 500001 for _ in range(2)]
        q: deque = deque()
        time: int = 0
        visited[0][n] = 0
        q.append((n, time))

        while q:
            subin, time = q.popleft()
            next_time = time + 1
            if subin - 1 >= 0 and visited[next_time % 2][subin - 1] == -1:
                q.append((subin - 1, next_time))
                visited[next_time % 2][subin - 1] = next_time
            if subin + 1 <= 500000 and visited[next_time % 2][subin + 1] == -1:
                q.append((subin + 1, next_time))
                visited[next_time % 2][subin + 1] = next_time
            if subin * 2 <= 500000 and visited[next_time % 2][subin * 2] == -1:
                q.append((subin * 2, next_time))
                visited[next_time % 2][subin * 2] = next_time

        for i in range(1000):
            k += i
            if k > 500000:
                break
            for j in range(i % 2, i + 1, 2):
                if visited[j % 2][k] != -1 and visited[j % 2][k] <= i:
                    ans = i
                    return ans
        return ans


if __name__ == "__main__":
    N: int
    K: int
    N, K = map(int, input().split())
    print(Solution.solve(N, K))
