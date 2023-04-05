from itertools import combinations


def get_chicken_dist(chicken_place: tuple[int, int], city: tuple[int, int]) -> int:
    ch_y, ch_x = chicken_place
    c_y, c_x = city
    return abs(ch_y - c_y) + abs(ch_x - c_x)


class Solution:
    @staticmethod
    def solve(n: int, m: int, city_info: list[list[int]]) -> int:
        ans: int = 1000000

        chicken_places: list[tuple[int, int]] = []
        cities: list[tuple[int, int]] = []
        for i in range(n):
            for j in range(n):
                if city_info[i][j] == 1:
                    cities.append((i, j))
                if city_info[i][j] == 2:
                    chicken_places.append((i, j))

        for selected in combinations(chicken_places, m):
            city_chicken_dist = 0
            for c in cities:
                c_dist = 1000000
                for s in selected:
                    c_dist = min(c_dist, get_chicken_dist(s, c))
                city_chicken_dist += c_dist
            ans = min(city_chicken_dist, ans)

        return ans


if __name__ == "__main__":
    N: int
    M: int
    city_info: list[list[int]]

    N, M = map(int, input().split())
    city_info = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, M, city_info))
