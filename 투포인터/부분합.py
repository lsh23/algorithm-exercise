class Solution:
    @staticmethod
    def solve(n: int, s: int, serial: list[int]) -> int:

        l = 0
        r = 0
        ans = 100001
        sum = serial[0]

        while True:
            if sum < S:
                r += 1
                if r == n:
                    break
                sum += serial[r]
            else:
                sum -= serial[l]
                ans = min(ans, r - l + 1)
                l += 1

        if ans == 100001:
            ans = 0

        return ans


if __name__ == "__main__":
    N: int
    S: int
    serial: list[int]
    N, S = map(int, input().split())
    serial = [int(x) for x in input().split()]
    print(Solution.solve(N, S, serial))
