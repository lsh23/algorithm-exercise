class Solution:
    def solve(self, M:int, N:int, lengths: list[int]):

        l: int = 1
        r: int = max(lengths)

        ans: int = 0

        while l <= r:

            mid = (l+r)//2
            tmp = 0
            for length in lengths:
                tmp += (length // mid)

            if tmp >= M:
                ans = mid
                l = mid + 1

            else:
                r = mid - 1

        return ans


if __name__ == '__main__':
    N: int
    M: int
    M, N = map(int, input().split())
    lengths: list[int] = [int(x) for x in input().split()]
    s: Solution = Solution()
    print(s.solve(M, N, lengths))

