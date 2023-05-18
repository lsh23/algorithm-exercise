def put_rest_area(n: int, m: int, l: int, rest_area: list[int], min_dist: int) -> bool:
    put_cnt: int = 0

    prev: int = 0
    for area in rest_area:
        while area > prev + min_dist:
            prev = prev + min_dist
            put_cnt += 1
        prev = area

    while l - 1 >= prev + min_dist:
        prev = prev + min_dist
        put_cnt += 1

    return put_cnt <= m


class Solution:
    @staticmethod
    def solve(n: int, m: int, l: int, rest_area: list[int]) -> int:
        rest_area.sort()
        left: int = 1
        right: int = l - 1
        ans: int = right
        while left <= right:
            mid = (left + right) // 2
            if put_rest_area(n, m, l, rest_area, mid):
                right = mid - 1
                ans = min(mid, ans)
            else:
                left = mid + 1
        return ans


if __name__ == "__main__":
    N: int
    M: int
    L: int
    rest_area: list[int]
    N, M, L = map(int, input().split())
    rest_area = [int(x) for x in input().split()]
    print(Solution.solve(N, M, L, rest_area))
