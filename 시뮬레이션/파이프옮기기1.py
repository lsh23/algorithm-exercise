class Solution:
    @staticmethod
    def solve(n: int, house_info: list[list[int]]) -> int:
        ans: int = 0
        pipe_end_y: int = 0
        pipe_end_x: int = 1
        pipe_direction: int = 0  # 0 가로, 1 세로, 2 대각선

        def move(end_y: int, end_x: int, direction: int):
            nonlocal ans
            if end_y == n - 1 and end_x == n - 1:
                ans += 1
                return

            if direction == 0 or direction == 2:
                if end_x + 1 < n and house_info[end_y][end_x + 1] == 0:
                    move(end_y, end_x + 1, 0)

            if direction == 1 or direction == 2:
                if end_y + 1 < n and house_info[end_y + 1][end_x] == 0:
                    move(end_y + 1, end_x, 1)

            if end_y + 1 < n and end_x + 1 < n:
                if house_info[end_y + 1][end_x + 1] == 0 and house_info[end_y + 1][end_x] == 0 and house_info[end_y][
                    end_x + 1] == 0:
                    move(end_y + 1, end_x + 1, 2)

        move(pipe_end_y, pipe_end_x, pipe_direction)
        return ans


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N: int
    house_info: list[list[int]]
    N = int(input())
    house_info = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, house_info))