class Solution:
    def solve(self, N:int, M:int, heights: list[int]) -> int:
        l: int = 1
        r: int = max(heights)
        ans: int = 0

        while l <= r:
            mid = (l+r) // 2
            if M <= sum([(h-mid) for h in heights if h > mid]):
                l = mid+1
                ans = mid
            else:
                r = mid-1

        return ans


if __name__ == '__main__':
    N: int
    M: int
    N, M = map(int, input().split())
    heights: list[int] = [int(x) for x in input().split()]
    s: Solution = Solution()
    print(s.solve(N, M, heights))