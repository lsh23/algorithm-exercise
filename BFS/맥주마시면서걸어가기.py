from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, s_y: int, s_x: int, f_y: int, f_x: int, convenience: list[tuple[int, int]]) -> str:
        convenience.sort()
        visited: list[int] = [0] * len(convenience)
        q: deque[tuple[int, int]] = deque()
        q.append((s_y, s_x))

        while q:
            y, x = q.popleft()

            if abs(f_y - y) + abs(f_x - x) <= 1000:
                return "happy"

            for i in range(len(convenience)):

                if visited[i] != 0:
                    continue

                c_y, c_x = convenience[i]

                if abs(c_y - y) + abs(c_x - x) <= 1000:
                    visited[i] = 1
                    q.append((c_y, c_x))

        return "sad"


if __name__ == "__main__":
    t: int
    t = int(input())
    for _ in range(t):
        n: int
        s_y: int
        s_x: int
        f_y: int
        f_x: int
        convenience: list[tuple[int, int], int] = []

        n = int(input())
        s_y, s_x = map(int, input().split())
        for _ in range(n):
            c_y, c_x = map(int, input().split())
            convenience.append((c_y, c_x))
        f_y, f_x = map(int, input().split())

        print(Solution.solve(n, s_y, s_x, f_y, f_x, convenience))
