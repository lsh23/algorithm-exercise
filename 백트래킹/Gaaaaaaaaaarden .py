import sys
from typing import List, Tuple
from collections import deque
class Solution:
    def solve(self, N:int, M:int, G:int, R:int, garden: List[List[int]]) -> int:

        points:List[Tuple[int]] = []

        for i in range(N):
            for j in range(M):
                if garden[i][j] == 2:
                    points.append((i,j))


        L: int = len(points)


        visited: List[int] = [0]*L

        dy = [0,1,0,-1]
        dx = [1,0,-1,0]

        global max_flower
        max_flower = 0

        def select_r(l:int, cnt:int, arr:List[int], g_arr:List[int]):
            global max_flower
            if cnt == R:
                q = deque()
                tmp = [[0]*M for _ in range(N)]
                for i in g_arr:
                    y = points[i][0]
                    x = points[i][1]
                    tmp[y][x] = 1
                    q.append((y, x))
                for i in arr:
                    y = points[i][0]
                    x = points[i][1]
                    tmp[y][x] = -1
                    q.append((y, x))

                flower = 0

                while q:
                    cur = q.popleft()
                    cur_y = cur[0]
                    cur_x = cur[1]
                    if tmp[cur_y][cur_x] == "F": continue
                    is_G = tmp[cur_y][cur_x] > 0
                    for i in range(4):
                        next_y = cur_y + dy[i]
                        next_x = cur_x + dx[i]
                        # 범위
                        if next_y < 0 or next_y >=N or next_x < 0 or next_x >= M: continue
                        # 호수
                        if garden[next_y][next_x] == 0: continue
                        if tmp[next_y][next_x] == "F": continue
                        if tmp[next_y][next_x] == 0:
                            if is_G:
                                tmp[next_y][next_x] = tmp[cur_y][cur_x] + 1
                            else:
                                tmp[next_y][next_x] = tmp[cur_y][cur_x] - 1
                            q.append((next_y, next_x))
                        elif tmp[next_y][next_x] < 0:
                            if is_G and tmp[next_y][next_x] + tmp[cur_y][cur_x] + 1 == 0:
                                tmp[next_y][next_x] = "F"
                                flower += 1
                        else:
                            if is_G is False and tmp[next_y][next_x] + tmp[cur_y][cur_x] - 1 == 0:
                                tmp[next_y][next_x] = "F"
                                flower += 1

                max_flower = max(max_flower,flower)
            else:
                for i in range(l,L):
                    if visited[i] == 0:
                        arr.append(i)
                        visited[i] = 1
                        select_r(i + 1, cnt + 1, arr, g_arr)
                        visited[i] = 0
                        arr.pop()

        def select_g(l:int, cnt:int, arr:List[int]):
            if cnt == G:
                select_r(0,0,[],arr)
            else:
                for i in range(l,L):
                    if visited[i] == 0:
                        arr.append(i)
                        visited[i]=1
                        select_g(i+1,cnt+1, arr)
                        visited[i]=0
                        arr.pop()

        select_g(0,0,[])


        return max_flower

if __name__ == '__main__':
    input = sys.stdin.readline
    N:int
    M:int
    G:int
    R:int
    N,M,G,R = map(int,input().split())

    garden: List[List[int]]
    garden = [ [int(x) for x in input().split()] for _ in range(N) ]

    s :Solution = Solution()

    answer :int = s.solve(N,M,G,R,garden)

    print(answer)