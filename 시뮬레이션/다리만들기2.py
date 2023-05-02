from collections import deque
import heapq

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def prim(v: int, graph: list[list[tuple[int, int]]]) -> int:
    checked: list[int] = [0] * v
    checked[0] = 1
    total_weight: int = 0

    q: list[tuple[int, int, int]] = []

    for edge in graph[0]:
        end, weight = edge
        heapq.heappush(q, (weight, 0, end))

    while not all(checked):
        if q:
            weight, start, end = heapq.heappop(q)
            if checked[end] != 0:
                continue
            checked[end] = 1
            total_weight += weight
            for edge in graph[end]:
                next_end, weight = edge
                heapq.heappush(q, (weight, end, next_end))
        else:
            break

    if not all(checked):
        return -1

    return total_weight


def get_all_bridge(n: int, m: int, map_info: list[list[int]]) -> list[tuple[int, int, int]]:
    bridges: set[tuple[int, int, int]] = set()
    checked: list[list[int]] = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if map_info[i][j] != 0 and checked[i][j] == 0:
                checked[i][j] = 1
                island_number = map_info[i][j]
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        continue
                    if map_info[ny][nx] != 0:
                        continue
                    length: int = 0
                    while True:
                        length += 1
                        ny = ny + dy[k]
                        nx = nx + dx[k]
                        if ny < 0 or ny >= n or nx < 0 or nx >= m:
                            break
                        if map_info[ny][nx] == island_number:
                            break
                        if map_info[ny][nx] != 0:
                            if length < 2:
                                break
                            bridges.add((length, island_number, map_info[ny][nx]))
                            break
    return bridges


def bridges_to_graph(bridges: set[tuple[int, int, int]], island_cnt: int) -> list[list[tuple[int, int]]]:
    graph: list[list[tuple[int, int]]] = [[] for _ in range(island_cnt)]
    for b in bridges:
        weight, start, end = b
        graph[start - 1].append((end - 1, weight))
        graph[end - 1].append((start - 1, weight))
    return graph


def get_island_cnt(map_info: list[list[int]], n: int, m: int) -> int:
    visited: list[list[int]] = [[0] * m for _ in range(n)]
    island_cnt: int = 0
    for i in range(n):
        for j in range(m):
            if map_info[i][j] == 1 and visited[i][j] == 0:
                island_cnt += 1
                q: deque[int] = deque()
                q.append((i, j))
                map_info[i][j] = island_cnt
                visited[i][j] = 1
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if ny < 0 or ny >= n or nx < 0 or nx >= m:
                            continue
                        if visited[ny][nx] != 0:
                            continue
                        if map_info[ny][nx] == 0:
                            continue
                        visited[ny][nx] = 1
                        map_info[ny][nx] = island_cnt
                        q.append((ny, nx))
    return island_cnt


class Solution:
    @staticmethod
    def solve(n: int, m: int, map_info: list[list[int]]) -> int:
        ans: int = 101

        # 섬에 번호 붙이기
        island_cnt: int = get_island_cnt(map_info, n, m)

        # 다리 후보군 구하기
        bridges: set[tuple[int, int, int]] = get_all_bridge(n, m, map_info)

        # bridges to graph
        graph: list[list[tuple[int, int]]] = bridges_to_graph(bridges, island_cnt)

        ans = prim(island_cnt, graph)

        return ans


if __name__ == "__main__":
    N: int
    M: int
    map_info: list[list[int]]
    N, M = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, M, map_info))
