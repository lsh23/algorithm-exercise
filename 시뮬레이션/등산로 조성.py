from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


class Solution:
    @staticmethod
    def solve(n, k, map_info) -> int:

        max_lenght = 0

        max_h = max([max(row) for row in map_info])
        start_points = []
        for i in range(n):
            for j in range(n):
                if map_info[i][j] == max_h:
                    start_points.append((i, j, 1))

        for i in range(n):
            for j in range(n):
                for m in range(1, k + 1):
                    copied_map_info = [[x for x in y] for y in map_info]
                    copied_map_info[i][j] -= m
                    # 가장 높은 봉우리 에서 시작
                    for start_point in start_points:
                        q = deque()
                        q.append(start_point)
                        while q:
                            y, x, l = q.popleft()
                            max_lenght = max(l, max_lenght)
                            for o in range(4):
                                ny = y + dy[o]
                                nx = x + dx[o]
                                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                                    continue
                                    # 높은 지형에서 낮은 지형 (같으면 안됨)
                                if copied_map_info[y][x] <= copied_map_info[ny][nx]:
                                    continue
                                q.append((ny, nx, l + 1))

        return max_lenght


if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        N, K = map(int, input().split())
        map_info = [[int(x) for x in input().split()] for _ in range(N)]
        ans = Solution.solve(N, K, map_info)
        print(f'#{test_case} {ans}')
