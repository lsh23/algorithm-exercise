dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


class Solution:
    @staticmethod
    def divide(n: int, x: int, y: int, d1: int, d2: int) -> list[list[int]]:
        area: list[list[int]] = [[0] * n for _ in range(n)]
        for i in range(d1 + 1):
            area[x + i][y - i] = 5
            area[x + d2 + i][y + d2 - i] = 5
        for i in range(d2 + 1):
            area[x + i][y + i] = 5
            area[x + d1 + i][y - d1 + i] = 5
        for i in range(x - 1, -1, -1):
            area[i][y] = 1
        for i in range(y - d1 - 1, -1, -1):
            area[x + d1][i] = 3
        for i in range(y + d2 + 1, n):
            area[x + d2][i] = 2
        for i in range(x + d1 + d2 + 1, n):
            area[i][y + d2 - d1] = 4
        return area

    @staticmethod
    def fill(point: tuple[int, int], number: int, area: list[list[int]]):
        n = len(area)
        y, x = point

        def dfs(y: int, x: int):
            if y < 0 or y >= n or x < 0 or x >= n:
                return
            if area[y][x] != 0:
                return
            area[y][x] = number
            dfs(y + 1, x)
            dfs(y, x - 1)
            dfs(y - 1, x)
            dfs(y, x + 1)

        dfs(y, x)

    @staticmethod
    def solve(n: int, a_r_c: list[list[int]]) -> int:
        # 전체 인구수
        ans: int = 500001
        # 선거구 나누는 방법 구하기
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                for x in range(n):
                    for y in range(n):
                        if x + d1 + d2 >= n or y - d1 < 0 or y + d2 >= n:
                            continue
                        # 선거구 나누기
                        area: list[list[int]] = Solution.divide(n, x, y, d1, d2)

                        # 구역 번호 채우기
                        Solution.fill((0, 0), 1, area)
                        Solution.fill((0, n - 1), 2, area)
                        Solution.fill((n - 1, 0), 3, area)
                        Solution.fill((n - 1, n - 1), 4, area)

                        # 인구수 세기
                        people: list[int] = [0] * 6
                        for i in range(n):
                            for j in range(n):
                                people[area[i][j]] += a_r_c[i][j]
                        people[5] += people[0]

                        # 인구수 최대 최소 구하기
                        people_max: int = max(people[1:])
                        people_min: int = min(people[1:])

                        # 차이 최솟값 갱신
                        ans = min(people_max - people_min, ans)

        return ans


if __name__ == "__main__":
    N: int
    A_r_c: list[list[int]]
    N = int(input())
    A_r_c = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, A_r_c))
