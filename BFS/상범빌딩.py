from collections import deque

dz = [0, 0, 0, 0, 1, -1]
dy = [0, 1, 0, -1, 0, 0]
dx = [1, 0, -1, 0, 0, 0]


class Solution:
    def solve(self, l: int, r: int, c: int, building:list[list[list[str]]]) -> str:
        ans: int = -1
        start: tuple[int,int,int]
        end: tuple[int,int,int]

        for i in range(l):
            for j in range(r):
                for k in range(c):
                    if building[i][j][k] == 'S':
                        start = (i, j, k)
                    if building[i][j][k] == 'E':
                        end = (i, j, k)

        visited: list[list[list[int]]] = [[[0] * c for _ in range(r)] for _ in range(l)]
        visited[start[0]][start[1]][start[2]] = 1
        q: deque[tuple[tuple[int,int,int], int]] = deque()
        q.append((start, 0))

        while q:

            cur = q.popleft()
            z = cur[0][0]
            y = cur[0][1]
            x = cur[0][2]
            d = cur[1]

            if end[0] == z and end[1] == y and end[2] == x:
                ans = d
                break

            for i in range(6):
                next_z = z + dz[i]
                next_y = y + dy[i]
                next_x = x + dx[i]

                if next_z < 0 or next_z >= l:
                    continue
                if next_y < 0 or next_y >= r:
                    continue
                if next_x < 0 or next_x >= c:
                    continue
                if visited[next_z][next_y][next_x] != 0:
                    continue
                if building[next_z][next_y][next_x] == '#':
                    continue
                visited[next_z][next_y][next_x] = 1

                q.append(((next_z, next_y, next_x),d+1))

        if ans != -1:
            return f'Escaped in {ans} minute(s).'

        return 'Trapped!'


if __name__ == "__main__" :

    L: int
    R: int
    C: int

    while True:
        L, R, C = map(int, input().split())

        if L == R == C == 0:
            break

        building = [[[] for _ in range(R)] for _ in range(L)]
        for i in range(L):
            for j in range(R):
                building[i][j] = [x for x in input() ]
            input()

        s: Solution = Solution()
        print(s.solve(L, R, C, building))