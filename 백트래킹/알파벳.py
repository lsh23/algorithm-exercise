dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


class Solution:
    @staticmethod
    def solve(r: int, c: int, board: list[list[int]]) -> int:
        answer: int = 0
        visited: list[int] = [0] * 26
        visited[board[0][0]] = 1

        def dfs(l: int, y: int, x: int):
            nonlocal answer
            if answer == 26:
                return
            else:
                answer = max(l, answer)
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= r or nx < 0 or nx >= c:
                        continue
                    if visited[board[ny][nx]] != 0:
                        continue
                    visited[board[ny][nx]] = 1
                    dfs(l + 1, ny, nx)
                    visited[board[ny][nx]] = 0

        dfs(1, 0, 0)
        return answer


if __name__ == "__main__":
    R: int
    C: int
    board: list[list[str]]
    R, C = map(int, input().split())
    board = [[ord(x) - ord('A') for x in input()] for _ in range(R)]
    print(Solution.solve(R, C, board))
