from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, l: int, r: int, A_r_c: list[list[int]]) -> int:

        dy = [0, -1, 0, 1]
        dx = [1, 0, -1, 0]
        # 인구 이동이 안일어 날떄 까지
        day: int = 0
        while True:
            visited: list[list[int]] = [[0] * n for _ in range(n)]
            q: deque[tuple[int, int]] = deque()
            union_number: int = 1
            union_number_to_population: dict[int ,int] = {}
            new_union: bool = False

            # print("before")
            # for a in A_r_c:
            #     print(a)
            # 인구 이동 BFS
            for i in range(n):
                for j in range(n):
                    if visited[i][j] == 0:
                        sum: int = A_r_c[i][j]
                        cnt: int = 1
                        visited[i][j] = union_number
                        q.append((i, j))
                        while q:
                            y, x = q.popleft()
                            for k in range(4):
                                ny = y + dy[k]
                                nx = x + dx[k]
                                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                                    continue
                                if visited[ny][nx] != 0:
                                    continue
                                diff: int = abs(A_r_c[y][x] - A_r_c[ny][nx])
                                if l <= diff <= r:
                                    visited[ny][nx] = union_number
                                    q.append((ny,nx))
                                    sum += A_r_c[ny][nx]
                                    cnt += 1
                                    new_union = True
                        union_number_to_population[union_number] = sum // cnt
                        union_number += 1
            if not new_union:
                break

            for i in range(n):
                for j in range(n):
                    if visited[i][j] != 0:
                        number = visited[i][j]
                        A_r_c[i][j] = union_number_to_population[number]

            # print("after")
            # for a in A_r_c:
            #     print(a)

            day += 1
        return day


if __name__ == "__main__":
    N: int
    L: int
    R: int
    A_r_c: list[list[int]]
    N, L, R = map(int, input().split())
    A_r_c = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, L, R, A_r_c))
