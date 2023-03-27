from collections import deque


class Solution:
    def solve(self, N: int, map_info: list[list[int]]) -> int:

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        visited: list[list[int]] = [[0] * N for _ in range(N)]
        q: deque = deque()
        island_cnt: int = 1

        # 섬 마다 번호 라벨링
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0 and map_info[i][j] == 1:
                    visited[i][j] == 1
                    map_info[i][j] = island_cnt
                    q.append((i, j, island_cnt))
                    while q:
                        y, x, island_no = q.popleft()
                        for k in range(4):
                            next_y = y + dy[k]
                            next_x = x + dx[k]
                            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= N:
                                continue
                            if map_info[next_y][next_x] == 0:
                                continue
                            if visited[next_y][next_x] == 1:
                                continue
                            visited[next_y][next_x] = 1
                            map_info[next_y][next_x] = island_no
                            q.append((next_y, next_x, island_no))
                    island_cnt += 1

        # for x in map_info:
        #     print(x)

        # 각 섬의 끝점을 가지고 BFS를 하며 인접 섬 까지의 최소거리 구하기
        ans: int = 201

        for k in range(1, island_cnt):
            visited = [[0] * N for _ in range(N)]

            for i in range(N):
                for j in range(N):
                    if map_info[i][j] == k:
                        visited[i][j] = 1
                        q.append((i, j, 0))

            # print(q)
            while q:
                y, x, l = q.popleft()
                for i in range(4):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if next_y < 0 or next_y >= N or next_x < 0 or next_x >= N:
                        continue
                    if visited[next_y][next_x] != 0:
                        continue
                    if map_info[next_y][next_x] != 0 and map_info[y][x] != map_info[next_y][next_x]:
                        ans = min(ans, l)
                        break
                    visited[next_y][next_x] = l+1
                    q.append((next_y, next_x, l+1))

            # for v in visited:
            #     print(v)

        return ans


if __name__ == '__main__':
    N: int = int(input())
    map_info: list[list[int]] = [[int(x) for x in input().split()] for _ in range(N)]
    s: Solution = Solution()
    print(s.solve(N, map_info))
