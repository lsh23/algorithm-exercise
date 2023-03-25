from collections import deque


class Solution:
    def solve(self, n: int, m: int, map_info: list[list[int]]) -> int:

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        ans: int = -1

        dist: list[list[int]] = [[[0] * M for _ in range(N)] for _ in range(2)]

        q: deque[tuple[int, int, int]] = deque()
        q.append((0, 0, 0))
        dist[0][0][0] = 1
        dist[1][0][0] = 1

        while q:

            break_cnt, y, x = q.popleft()
            if y == n-1 and x == m-1:
                ans = dist[break_cnt][y][x]
                break

            for i in range(4):
                next_y = y + dy[i]
                next_x = x + dx[i]
                if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                    continue

                if dist[break_cnt][next_y][next_x] != 0:
                    continue

                if map_info[next_y][next_x] == 0:
                    q.append((break_cnt, next_y, next_x))
                    dist[break_cnt][next_y][next_x] = dist[break_cnt][y][x]+1

                if map_info[next_y][next_x] == 1 and break_cnt == 0:
                    q.append((break_cnt+1, next_y, next_x))
                    dist[break_cnt+1][next_y][next_x] = dist[break_cnt][y][x] + 1

            # print("non break---------------")
            # for x in dist[0]:
            #     print(x)
            #
            # print("break---------------")
            # for x in dist[1]:
            #     print(x)

        return ans


if __name__ == '__main__':
    N: int
    M: int
    N, M = map(int, input().split())
    map_info = [[int(x) for x in input()] for _ in range(N)]
    assert len(map_info) == N
    assert len(map_info[0]) == M
    s: Solution = Solution()
    print(s.solve(N, M, map_info))
