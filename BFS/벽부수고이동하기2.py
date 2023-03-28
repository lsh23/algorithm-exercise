from collections import deque


class Solution:
    def solve(self, n: int, m: int, k: int, map_info: list[list[int]]) -> int:

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        ans: int = -1

        visited: list[list[int]] = [[[0] * M for _ in range(N)] for _ in range(k + 1)]

        q: deque[tuple[int, int, int, int]] = deque()
        q.append((0, 0, 0, 1))
        for i in range(k + 1):
            visited[i][0][0] = 1

        while q:

            y, x, break_cnt, l = q.popleft()
            if y == n - 1 and x == m - 1:
                ans = l
                break

            for i in range(4):
                next_y = y + dy[i]
                next_x = x + dx[i]
                if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                    continue

                if visited[break_cnt][next_y][next_x] != 0:
                    continue

                if map_info[next_y][next_x] == 0:
                    q.append((next_y, next_x, break_cnt, l + 1))
                    visited[break_cnt][next_y][next_x] = 1

                if map_info[next_y][next_x] == 1 and break_cnt < k:
                    if visited[break_cnt + 1][next_y][next_x] == 0:
                        q.append((next_y, next_x, break_cnt + 1, l + 1))
                        visited[break_cnt + 1][next_y][next_x] = 1

        return ans


if __name__ == '__main__':
    N: int
    M: int
    K: int
    N, M, K = map(int, input().split())
    map_info = [[int(x) for x in input()] for _ in range(N)]
    assert len(map_info) == N
    assert len(map_info[0]) == M
    s: Solution = Solution()
    print(s.solve(N, M, K, map_info))
