from typing import List, Tuple
from collections import deque
class Solution:
    def solve(self, M:int ,N:int ,H:int,tomato:List[List[List[int]]] ) -> int:

        q = deque()
        for k in range(H):
            for i in range(N):
                for j in range(M):
                    if tomato[k][i][j] == 1:
                        q.append((k,i,j))

        dy = [0,-1,0,1,0,0]
        dx = [1,0,-1,0,0,0]
        dz = [0,0,0,0,1,-1]

        while q:
            cur = q.popleft()
            cur_z = cur[0]
            cur_y = cur[1]
            cur_x = cur[2]
            cur_distance = tomato[cur_z][cur_y][cur_x]
            for i in range(6):
                next_z = cur_z + dz[i]
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                if next_z < 0 or next_z >= H or next_y < 0 or next_y >= N or next_x < 0 or next_x >= M:
                    continue
                if tomato[next_z][next_y][next_x] == 0:
                    tomato[next_z][next_y][next_x] = cur_distance + 1
                    q.append((next_z,next_y,next_x))

        max_distance = 0

        for k in range(H):
            for i in range(N):
                for j in range(M):
                    max_distance = max(max_distance,tomato[k][i][j])
                    if tomato[k][i][j] == 0:
                        return -1

        return max_distance-1

if __name__ == '__main__':

    M:int
    N:int
    H:int

    M,N,H = map(int,input().split())

    tomato = [ [ [ int(x) for x in input().split() ] for _ in range(N) ] for _ in range(H) ]
    # print(tomato)

    s :Solution = Solution()
    answer :int = s.solve(M,N,H,tomato)
    print(answer)