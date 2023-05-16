def check(i: int, j: int, planets: list[list[int]]) -> bool:
    for k in range(N):
        if planets[i][k] != planets[j][k]:
            return False
    return True


class Solution:
    @staticmethod
    def solve(m: int, n: int, planets: list[list[int]]) -> int:
        cnt: int = 0
        for i in range(m):
            planet = planets[i]
            tmp_dict = {v: idx for idx, v in enumerate(sorted(list(set(planet))))}
            planet = [tmp_dict[x] for x in planet]
            planets[i] = planet

        for i in range(m - 1):
            for j in range(i + 1, m):
                if check(i, j, planets):
                    cnt += 1
        return cnt


if __name__ == "__main__":
    M: int
    N: int
    planets: list[list[int, int, int]]
    M, N = map(int, input().split())
    planets = [[int(x) for x in input().split()] for _ in range(M)]
    print(Solution.solve(M, N, planets))
