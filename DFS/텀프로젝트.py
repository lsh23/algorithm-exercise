import sys
sys.setrecursionlimit(10**6)


class Solution:
    def solve(self, n: int, students: list[int]) -> int:

        check: list[int] = [0] * (n + 1)
        visited: list[int] = [0] * (n + 1)
        ans: int = n

        def dfs(now: int):
            nonlocal ans
            next_student = students[now]
            if visited[next_student] != 0:
                if check[next_student] == 0:
                    ans -= 1
                    while next_student != now:
                        next_student = students[next_student]
                        ans -= 1
            else:
                visited[next_student] = 1
                dfs(next_student)

            check[now] = 1

        for i in range(1, n+1):
            if check[i] == 0:
                visited[i] = 1
                dfs(i)

        return ans


if __name__ == '__main__':
    T: int = int(input())
    for _ in range(T):
        n: int = int(input())
        students: list[int] = [0]
        students += [int(x) for x in input().split()]
        s: Solution = Solution()
        print(s.solve(n, students))
