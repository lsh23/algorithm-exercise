from collections import deque


class Solution:
    @staticmethod
    def solve(n: int, m: int, switch_info: list[list[int]]) -> int:

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        visited: list[list[int]] = [[0] * (n + 1) for _ in range(n + 1)]
        switch_on: list[list[int]] = [[0] * (n + 1) for _ in range(n + 1)]

        switch_info_map: dict[tuple[int,int], list[tuple[int,int]]]= {}

        for info in switch_info:
            room1 = (info[0], info[1])
            room2 = (info[2], info[3])
            if room1 in switch_info_map:
                switch_info_map[room1].append(room2)
            else:
                switch_info_map[room1] = [room2]

        q: deque = deque()
        # (1, 1) 에서 출발
        visited[1][1] = 1
        switch_on[1][1] = 1
        q.append((1, 1))

        while q:
            cur = q.popleft()
            y = cur[0]
            x = cur[1]

            # 1. 현재 위치의 스위치 조회
            for s in switch_info_map.get(cur, []):
                # 2. 스위치들로 전부 불 켜기
                switch_on[s[0]][s[1]] = 1
                for i in range(4):
                    prev_y = s[0] + dy[i]
                    prev_x = s[1] + dx[i]
                    if prev_y < 1 or prev_y > n or prev_x < 1 or prev_x > n:
                        continue
                    # 3. 스위치가 켜져 있는 방이면서 접근 가능한 지점으로 이동
                    if visited[prev_y][prev_x] == 1 and visited[s[0]][s[1]] == 0:
                        visited[s[0]][s[1]] = 1
                        q.append((s[0], s[1]))

            for i in range(4):
                next_y = y + dy[i]
                next_x = x + dx[i]
                if next_y < 1 or next_y > n or next_x < 1 or next_x > n:
                    continue
                if switch_on[next_y][next_x] == 0:
                    continue
                if visited[next_y][next_x] != 0:
                    continue
                # 3. 현재 위치에서 인접한 방들 중에서 불켜진곳으로 이동
                visited[next_y][next_x] = 1
                q.append((next_y, next_x))

            # for s in switch_on:
            #     print(s)

        cnt: int = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if switch_on[i][j]:
                    cnt += 1

        return cnt


if __name__ == "__main__":
    N: int
    M: int
    switch_info: list[list[int]]

    N, M = map(int, input().split())
    switch_info = [[int(x) for x in input().split()] for _ in range(M)]
    assert len(switch_info) == M and len(switch_info[0]) == 4
    print(Solution.solve(N, M, switch_info))
