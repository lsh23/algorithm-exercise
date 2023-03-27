from collections import deque


class Solution:
    def solve(self, n: int, k: int) -> int:
        ans: int = 100001

        q: deque = deque()
        visited: list[int] = [0] * 200001

        visited[n] = 1
        q.append((n, 0))

        while q:
            cur_position, time = q.popleft()

            if cur_position == k:
                ans = min(ans, time)

            if cur_position - 1 >= 0:
                if visited[cur_position-1] == 0:
                    visited[cur_position-1] = 1
                    q.append((cur_position-1, time+1))

            if cur_position * 2 <= 200000:
                if visited[cur_position*2] == 0:
                    visited[cur_position*2] = 1
                    q.append((cur_position*2, time))

            if cur_position + 1 <= 200000:
                if visited[cur_position+1] == 0:
                    visited[cur_position+1] = 1
                    q.append((cur_position+1, time+1))

        return ans


if __name__ == '__main__':
    N: int
    K: int
    N, K = map(int, input().split())
    s: Solution = Solution()
    print(s.solve(N, K))
