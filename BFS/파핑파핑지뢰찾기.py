from collections import deque

dy = [0, 0, -1, -1, -1, 1, 1, 1]
dx = [-1, 1, -1, 0, 1, -1, 0, 1]


class Solution:
    @staticmethod
    def solve(n, map_info):
        cnt = 0
        q = deque()
        visited = [[0] * n for _ in range(N)]
        for i in range(n):
            for j in range(n):
                if map_info[i][j] != '.':
                    continue
                if visited[i][j] != 0:
                    continue
                adj_boom_cnt = 0
                for k in range(8):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue
                    if visited[ny][nx] != 0:
                        continue
                    if map_info[ny][nx] == '*':
                        adj_boom_cnt += 1
                if adj_boom_cnt != 0:
                    continue
                cnt += 1
                visited[i][j] = 1
                for k in range(8):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue
                    if visited[ny][nx] != 0:
                        continue
                    if map_info[ny][nx] != '.':
                        continue
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                while q:
                    y, x = q.popleft()
                    adj_boom_cnt = 0
                    for k in range(8):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if ny < 0 or ny >= n or nx < 0 or nx >= n:
                            continue
                        if visited[ny][nx] != 0:
                            continue
                        if map_info[ny][nx] == '*':
                            adj_boom_cnt += 1
                    if adj_boom_cnt != 0:
                        continue
                    for k in range(8):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if ny < 0 or ny >= n or nx < 0 or nx >= n:
                            continue
                        if visited[ny][nx] != 0:
                            continue
                        if map_info[ny][nx] != '.':
                            continue
                        visited[ny][nx] = 1
                        q.append((ny, nx))

        # for v in visited:
        #     print(v)
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0 and map_info[i][j] == '.':
                    cnt += 1
        return cnt


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    map_info = [[x for x in input()] for _ in range(N)]
    answer = Solution.solve(N, map_info)
    print(f'#{test_case} {answer}')
