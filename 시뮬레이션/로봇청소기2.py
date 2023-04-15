from collections import deque
from itertools import permutations

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
DIRTY = "*"
CLEANED = "."
FURNITURE = "x"
ROBOT = "o"


class Solution:
    @staticmethod
    def solve(w: int, h: int, room_info: list[list[str]]) -> int:

        ans: int = 1000000000
        # 로봇은 더러운 칸을 방문해서 깨끗한 칸으로 바꿀수 있음
        # 가구가 놓여진 칸으로는 이동 불가
        # 한번 움찍일 때 상하좌우 중 인접한 한 칸으로 이동, 같은 칸 여러번 방문 가능
        # 더러운 칸을 모두 깨끗한 칸으로 만드는데 필요한 이동횟수의 최솟값

        # 시작점과 더러운칸들로 가중치 그래프를 그린다.
        # 10 * WH(BFS) 모든 점들간 거리 구하기
        start_point: tuple[int, int]
        dirty_blocks: list[tuple[int, int]] = []
        for i in range(h):
            for j in range(w):
                if room_info[i][j] == DIRTY:
                    dirty_blocks.append((i, j))
                if room_info[i][j] == ROBOT:
                    start_point = (i, j)

        dist_from_start_to_dirty_blocks: list[int] = [0] * len(dirty_blocks)
        graph: list[list[int]] = [[0] * len(dirty_blocks) for _ in range(len(dirty_blocks))]

        for i in range(len(dirty_blocks)):
            q: deque[tuple[int, int]] = deque()
            dirty_block = dirty_blocks[i]
            q.append(dirty_block)
            dist: list[list[int]] = [[-1] * w for _ in range(h)]
            dist[dirty_block[0]][dirty_block[1]] = 0
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if ny < 0 or ny >= h or nx < 0 or nx >= w:
                        continue
                    if room_info[ny][nx] == FURNITURE:
                        continue
                    if dist[ny][nx] != -1:
                        continue
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

            dist_from_start_to_dirty_blocks[i] = dist[start_point[0]][start_point[1]]
            for j in range(i + 1, len(dirty_blocks)):
                y, x = dirty_blocks[j]
                graph[i][j] = dist[y][x]
                graph[j][i] = dist[y][x]

        # print(dist_from_start_to_dirty_blocks)
        # for g in graph:
        #     print(g)

        # 최대 10개의 더러운칸을 방문하는 모든 순서의 경우의 수 10!
        for order in permutations([i for i in range(len(dirty_blocks))]):
            if dist_from_start_to_dirty_blocks[order[0]] == -1:  # 시작점에서 첫번째 더러운 칸 접근이 불가능한 경우
                continue

            total_dist: int = dist_from_start_to_dirty_blocks[order[0]]

            stop: bool = False
            for i in range(1, len(order)):
                if graph[order[i - 1]][order[i]] == -1:  # 다음 더러운 칸으로 접근 불가는 한 경우
                    stop = True
                    break
                total_dist += graph[order[i - 1]][order[i]]

            if stop:
                continue

            ans = min(total_dist, ans)

        if ans == 1000000000:
            return -1
        return ans


if __name__ == "__main__":
    w: int
    h: int
    room_info: list[list[str]]
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        room_info = [[x for x in input()] for _ in range(h)]
        print(Solution.solve(w, h, room_info))
