from collections import deque


class Solution:
    def solve(self, k: int, w: int, h: int, map_info: list[list[int]]) -> int:

        ans: int = -1

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        horse_dy = [1, 1, 2, 2, -2, -2, -1, -1]
        horse_dx = [-2, 2, -1, 1, -1, 1, -2, 2]

        visited: list[list[int]] = [[[0] * w for _ in range(h)] for _ in range(k+1)]

        q: deque = deque()
        q.append((0, 0, 0, 0))
        visited[0][0][0] = 1

        while q:
            y, x, horse_step, l = q.popleft()
            if y == h - 1 and x == w - 1:
                ans = l
                break

            for i in range(4):
                next_y = y + dy[i]
                next_x = x + dx[i]
                if next_y < 0 or next_y >= h or next_x < 0 or next_x >= w:
                    continue
                if map_info[next_y][next_x] != 0:
                    continue
                if visited[horse_step][next_y][next_x] != 0:
                    continue
                q.append((next_y, next_x, horse_step, l + 1))
                visited[horse_step][next_y][next_x] = 1

            if horse_step < k:
                for i in range(8):
                    next_y = y + horse_dy[i]
                    next_x = x + horse_dx[i]
                    if next_y < 0 or next_y >= h or next_x < 0 or next_x >= w:
                        continue
                    if map_info[next_y][next_x] != 0:
                        continue
                    if visited[horse_step+1][next_y][next_x] != 0:
                        continue
                    q.append((next_y, next_x, horse_step + 1, l + 1))
                    visited[horse_step+1][next_y][next_x] = 1

        return ans


if __name__ == '__main__':
    K: int
    W: int
    H: int
    map_info = list[list[int]]

    K = int(input())
    W, H = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(H)]

    assert len(map_info) == H
    assert len(map_info[0]) == W

    s: Solution = Solution()
    print(s.solve(K, W, H, map_info))
