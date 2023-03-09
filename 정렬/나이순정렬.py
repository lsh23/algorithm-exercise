class Solution:
    def solve(self, N:int, members:list[tuple[int, int, int]]):
        members.sort(key=lambda x: x[0])
        for m in members:
            print(m[0], m[1])


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    N: int = int(input())
    members: list[tuple[int, str]] = []
    for i in range(N):
        age, name = input().strip().split()
        members.append((int(age),name))
    s: Solution = Solution()
    s.solve(N, members)
