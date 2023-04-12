from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, space_info: list[list[int]]) -> int:
        ans: int = 0
        size: int = 2
        eat_cnt: int = 0
        shark: tuple[int, int, int, int]
        # 아기 상어 초기 위치 구하기
        for i in range(n):
            for j in range(n):
                if space_info[i][j] == 9:
                    shark = (i, j)
                    space_info[i][j] = 0
                    break

        dy = [-1, 0, 0, 1]
        dx = [0, -1, 1, 0]

        can_eat: bool = True
        while can_eat:  # 더 이상 먹을 수 있는 물고기가 공간에 없을 때 까지 - end 조건
            # 물고기 탐색 - BFS
            dist: list[list[int]] = [[-1] * n for _ in range(n)]
            q: deque[tuple[int, int, int, int]] = deque()
            q.append(shark)
            dist[shark[0]][shark[1]] = 0
            can_eat = False
            d: int = 401
            next_y = 21
            next_x = 21
            while q:
                y, x = q.popleft()
                if space_info[y][x] != 0 and space_info[y][x] < size:
                    can_eat = True
                    if dist[y][x] < d:
                        d = dist[y][x]
                        next_y = y
                        next_x = x
                    elif dist[y][x] == d:
                        if y < next_y:
                            next_y = y
                            next_x = x
                        elif y == next_y and x < next_x:
                            next_x = x
                    continue
                # 방문 순서는 ^ < > v 로
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue
                    # 이미 방문했거나,
                    if dist[ny][nx] != -1:
                        continue
                    # 자신보다 큰 물고기가 있으면 방문 못함
                    if size < space_info[ny][nx]:
                        continue
                    q.append((ny, nx))
                    dist[ny][nx] = dist[y][x] + 1

            if can_eat:
                space_info[next_y][next_x] = 0
                eat_cnt += 1
                if eat_cnt == size:
                    size += 1
                    eat_cnt = 0
                shark = (next_y, next_x)
                ans += dist[next_y][next_x]

        return ans


if __name__ == "__main__":
    N: int
    space_info: list[list[int]]
    N = int(input())
    space_info = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, space_info))
