def check(l: int, xn: list[int]) -> bool:
    prev: int = xn[0]
    cnt: int = 1
    for i in range(1, N):
        if xn[i] - prev >= l:
            cnt += 1
            prev = xn[i]
    return cnt >= C

class Solution:
    @staticmethod
    def solve(n: int, c: int, xn: list[int]) -> int:
        xn.sort()
        dist: list[int] = [0] * (n - 1)
        for i in range(n - 1):
            dist[i] = xn[i + 1] - xn[i]

        ans: int = 0
        l = 1
        r = xn[n-1] - xn[0]
        while l <= r:
            mid = (l + r) // 2
            if check(mid, xn):
                l = mid + 1
                ans = max(ans, mid)
            else:
                r = mid - 1
        return ans


if __name__ == "__main__":
    N: int
    C: int
    Xn: list[int]
    N, C = map(int, input().split())
    Xn = [int(input()) for _ in range(N)]
    print(Solution.solve(N, C, Xn))
