from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
class Solution:
    def solve(self, h:int, w:int, miro: list[list[str]]) -> int:
        # 상근과 불 각각 시작점에서 미로의 가장자리(탈출점)의 최단거리를 구했을 때 지훈이 더 작은 경우를 찾고 그 최솟값
        # 작은 경우가 없으면 불가능
        s_start: tuple[int, int]
        f_start: list(tuple[int, int]) = []

        for i in range(h):
            for j in range(w):
                if miro[i][j] == "@":
                    s_start = (i, j)
                if miro[i][j] == "*":
                    f_start.append((i, j))

        j_route: list[list[int]] = [[0]*w for _ in range(h)]
        s_visited: list[list[int]] = [[0]*w for _ in range(h)]

        q: deque[tuple[int, int]] = deque()
        q.append(s_start)
        s_visited[s_start[0]][s_start[1]] = 1

        while q:
            cur = q.popleft()
            y = cur[0]
            x = cur[1]
            for i in range(4):
                next_y = y + dy[i]
                next_x = x + dx[i]
                if next_x < 0 or next_x >= w or next_y < 0 or next_y >= h:
                    continue
                if s_visited[next_y][next_x]:
                    continue
                if miro[next_y][next_x] == "#":
                    continue
                s_visited[next_y][next_x] = 1
                j_route[next_y][next_x] = j_route[y][x] + 1
                q.append((next_y, next_x))

        f_route: list[list[int]] = [[0]*w for _ in range(h)]
        f_visited: list[list[int]] = [[0]*w for _ in range(h)]
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
                if next_x < 0 or next_x >= w or next_y < 0 or next_y >= h:
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

        for i in range(h):
            if s_visited[i][0] == 1 and (j_route[i][0] < f_route[i][0] or f_visited[i][0] == 0):
                ans = min(ans, j_route[i][0])
            if s_visited[i][w-1] == 1 and (j_route[i][w-1] < f_route[i][w-1] or f_visited[i][w-1] == 0):
                ans = min(ans, j_route[i][w-1])
        for i in range(w):
            if s_visited[0][i] == 1 and (j_route[0][i] < f_route[0][i] or f_visited[0][i] == 0):
                ans = min(ans, j_route[0][i])
            if s_visited[h-1][i] == 1 and (j_route[h-1][i] < f_route[h-1][i] or f_visited[h-1][i] == 0):
                ans = min(ans, j_route[h-1][i])

        if ans != 10**6:
            return ans+1

        return "IMPOSSIBLE"

if __name__ == '__main__':
    T: int = int(input())
    for _ in range(T):
        w: int
        h: int
        w, h = map(int, input().split())
        miro: list[list[str]] = [[x for x in input()] for _ in range(h)]
        assert len(miro) == h
        assert len(miro[0]) == w
        s: Solution = Solution()
        print(s.solve(h, w, miro))