class Solution:
    def solve(self, N:int, points:list[int]) -> int:
        ans: int = 0
        next_points = points[-1]
        for i in range(N-2,-1,-1):
            if points[i] >= next_points:
                ans = ans + (points[i]-next_points)+1
                next_points = next_points - 1
            else:
                next_points = points[i]
        return ans


if __name__ == '__main__':
    N: int = int(input())
    points: list[int] = [int(input()) for _ in range(N)]
    s: Solution = Solution()
    print(s.solve(N, points))