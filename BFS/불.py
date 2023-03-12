from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
class Solution:
    def solve(self, r:int, c:int, miro: list[list[str]]) -> int:
        # 지훈과 불 각각 시작점에서 미로의 가장자리(탈출점)의 최단거리를 구했을 때 지훈이 더 작은 경우를 찾고 그 최솟값
        # 작은 경우가 없으면 불가능
        j_start: tuple[int, int]
        f_start: list(tuple[int, int]) = []

        for i in range(r):
            for j in range(c):
                if miro[i][j] == "J":
                    j_start = (i, j)
                if miro[i][j] == "F":
                    f_start.append((i, j))

        j_route: list[list[int]] = [[0]*c for _ in range(r)]
        j_visited: list[list[int]] = [[0]*c for _ in range(r)]

        q: deque[tuple[int, int]] = deque()
        q.append(j_start)
        j_visited[j_start[0]][j_start[1]] = 1

        while q:
            cur = q.popleft()
            y = cur[0]
            x = cur[1]
            for i in range(4):
                next_y = y + dy[i]
                next_x = x + dx[i]
                if next_x < 0 or next_x >= c or next_y < 0 or next_y >= r:
                    continue
                if j_visited[next_y][next_x]:
                    continue
                if miro[next_y][next_x] == "#":
                    continue
                j_visited[next_y][next_x] = 1
                j_route[next_y][next_x] = j_route[y][x] + 1
                q.append((next_y, next_x))

        f_route: list[list[int]] = [[0]*c for _ in range(r)]
        f_visited: list[list[int]] = [[0]*c for _ in range(r)]
        q: deque[tuple[int, int]] = deque(f_start)

        for s in f_start:
            f_visited[s[0]][s[1]] = 1

        while q:
            cur = q.popleft()
            y = cur[0]
            x = cur[1]
            for i in range(4):
                next_y = y + dy[i]
                next_x = x + dx[i]
                if next_x < 0 or next_x >= c or next_y < 0 or next_y >= r:
                    continue
                if miro[next_y][next_x] == "#":
                    continue
                if f_visited[next_y][next_x] == 1:
                    continue
                f_visited[next_y][next_x] = 1
                f_route[next_y][next_x] = f_route[y][x] + 1
                q.append((next_y, next_x))

        ans: int = 10**6

        # for x in j_route:
        #     print(x)
        # print()
        # for x in f_route:
        #     print(x)

        for i in range(r):
            if j_visited[i][0] == 1 and (j_route[i][0] < f_route[i][0] or f_visited[i][0] == 0):
                ans = min(ans, j_route[i][0])
            if j_visited[i][c-1] == 1 and (j_route[i][c-1] < f_route[i][c-1] or f_visited[i][c-1] == 0):
                ans = min(ans, j_route[i][c-1])
        for i in range(c):
            if j_visited[0][i] == 1 and (j_route[0][i] < f_route[0][i] or f_visited[0][i] == 0):
                ans = min(ans, j_route[0][i])
            if j_visited[r-1][i] == 1 and (j_route[r-1][i] < f_route[r-1][i] or f_visited[r-1][i] == 0):
                ans = min(ans, j_route[r-1][i])

        if ans != 10**6:
            return ans+1

        return "IMPOSSIBLE"

if __name__ == '__main__':
    R: int
    C: int
    R, C = map(int, input().split())
    miro: list[list[str]] = [[x for x in input()] for _ in range(R)]
    assert len(miro) == R
    assert len(miro[0]) == C
    s: Solution = Solution()
    print(s.solve(R, C, miro))