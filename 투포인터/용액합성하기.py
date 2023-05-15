class Solution:
    @staticmethod
    def solve(n: int, a: list[int]) -> int:
        l = 0
        r = n - 1
        B: int = 200000001
        while l < r:
            tmp = a[l] + a[r]
            if tmp > 0:
                if abs(tmp) < abs(B):
                    B = tmp
                r -= 1
            elif tmp < 0:
                if abs(tmp) < abs(B):
                    B = tmp
                l += 1
            else:
                B = 0
                break

        return B


if __name__ == "__main__":
    N: int
    A: list[int]
    N = int(input())
    A = [int(x) for x in input().split()]
    print(Solution.solve(N, A))
