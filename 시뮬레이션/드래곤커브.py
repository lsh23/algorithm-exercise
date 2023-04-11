class Solution:
    @staticmethod
    def solve(n: int, d_curves: list[list[int]]) -> int:
        dy = [0, -1, 0, 1]
        dx = [1, 0, -1, 0]

        ans: int = 0
        # 0 세대 끝점 방향
        # 0
        # 1 세대
        # 0 1
        # 2 세대
        # 0 1 2 1
        # 3 세대
        # 0 1 2 1 2 3 2 1

        visited: list[list[int]] = [[0] * (101) for _ in range(101)]
        for d_curve in d_curves:
            x, y, d, g = d_curve

            dragon_curve_directions: list[int] = [d]
            for j in range(10):
                dragon_curve_directions = dragon_curve_directions + [(x + 1) % 4 for x in
                                                                     dragon_curve_directions[::-1]]
            visited[x][y] = 1
            for dir in dragon_curve_directions[:2 ** g]:
                nx = x + dx[dir]
                ny = y + dy[dir]
                visited[nx][ny] = 1
                x, y = nx, ny

        for i in range(100):
            for j in range(100):
                if visited[i][j] and visited[i + 1][j] and visited[i][j + 1] and visited[i + 1][j + 1]:
                    ans += 1

        return ans


if __name__ == "__main__":
    N: int
    dragon_curves: list[list[int]]
    N = int(input())
    dragon_curves = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, dragon_curves))
