from typing import List, Tuple
from collections import deque
class Solution:
    def solve(self, l: int, _from: Tuple[int,int], _to: Tuple[int,int] ) -> int:

        min_cnt: int = 300

        dy: List[int] = [1,1,-1,-1,2,2,-2,-2]
        dx: List[int] = [2,-2,2,-2,1,-1,1,-1]

        q: deque = deque()
        q.append((_from[0],_from[1],0))

        visited: List[List[int]] = [ [0]*l for _ in range(l) ]

        while q:
            cur = q.popleft()
            cur_y = cur[0]
            cur_x = cur[1]
            cur_cnt = cur[2]

            # print(cur_y, cur_x, cur_cnt)

            if cur_y == _to[0] and cur_x == _to[1]:
                min_cnt = min(min_cnt, cur_cnt)
                break
            for i in range(8):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                if next_y < 0 or next_y >= l or next_x < 0 or next_x >= l:
                    continue
                if visited[next_y][next_x] == 1:
                    continue
                visited[next_y][next_x] = 1
                q.append((next_y,next_x,cur_cnt+1))
            # print(q)

        return min_cnt

if __name__ == '__main__':

    T: int = int(input())

    for _ in range(T):
        l: int = int(input())
        _from: Tuple[int,int] = tuple(map(int,input().split()))
        _to: Tuple[int,int] = tuple(map(int,input().split()))

        s: Solution = Solution()
        print(s.solve(l,_from,_to))

