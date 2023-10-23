class Solution:
    @staticmethod
    def solve(n: int, m: int, budgets: list[int]) -> int:
        if sum(budgets) <= m:
            return max(budgets)

        l: int = 0
        r: int = max(budgets)

        answer: int = 0
        while l <= r:
            mid = (l + r) // 2

            b = [x if x <= mid else mid for x in budgets]
            if sum(b) <= m:
                answer = max(b)
                l = mid + 1
            else:
                r = mid - 1

        return answer


if __name__ == "__main__":
    N: int
    M: int
    budgets: list[int]
    N = int(input())
    budgets = [int(x) for x in input().split()]
    M = int(input())
    print(Solution.solve(N, M, budgets))
