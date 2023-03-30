from collections import deque


class Solution:
    @staticmethod
    def solve(w: int, h: int, building_info: list[list[str]], keys: dict[str, int]) -> int:

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        # 가장자리 외부점들
        start_points: list[tuple[int, int]] = []
        treasure: dict[tuple[int, int], int] = {}

        for i in range(0, w + 2):
            start_points.append((0, i))
            start_points.append((h + 1, i))
        for i in range(1, h + 1):
            start_points.append((i, 0))
            start_points.append((i, w + 1))

        while True:
            found_new_treasure: bool = False
            found_new_key: bool = False
            q: deque[tuple[int, int]] = deque(start_points)
            visited: list[list[int]] = [[0] * (w + 2) for _ in range(h + 2)]

            # 모든 출발점에 대해서 BFS로 새로운 열쇠 또는 문서 찾기
            while q:
                # 새로운 열쇠나 문서가 발견되지 않았으면 종료
                # 찾았으면 반복
                y, x = q.popleft()
                for i in range(4):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if next_y < 1 or next_y > h or next_x < 1 or next_x > w:
                        continue
                    if visited[next_y][next_x] != 0:
                        continue
                    if building_info[next_y][next_x] == '*':
                        continue
                    if 65 <= ord(building_info[next_y][next_x]) <= 90:  # 문
                        ## 통과할 수 없으면 continue
                        if building_info[next_y][next_x].lower() not in keys:
                            continue
                    if building_info[next_y][next_x] == '$':  # 보물
                        ## 새로운 보물
                        if (next_y, next_x) not in treasure:
                            treasure[(next_y, next_x)] = 1
                            found_new_treasure = True
                    if 97 <= ord(building_info[next_y][next_x]) <= 122:  # 열쇠
                        ## 새로운 열쇠
                        if building_info[next_y][next_x] not in keys:
                            keys[building_info[next_y][next_x]] = 1
                            found_new_key = True
                    visited[next_y][next_x] = 1
                    q.append((next_y, next_x))

            if not found_new_treasure and not found_new_key:
                break

        return len(treasure)


if __name__ == '__main__':
    T: int = int(input())
    for _ in range(T):
        w: int
        h: int
        h, w = map(int, input().split())
        building_info: list[list[str]] = [[0] + [x for x in input()] + [0] for _ in range(h)]
        building_info.insert(0, [0]*(w+2))
        building_info.append([0]*(w+2))
        assert len(building_info) == h+2 and len(building_info[0]) == w+2
        keys: dict = {}
        for x in input():
            if x not in keys:
                keys[x] = 1
        print(Solution.solve(w, h, building_info, keys))
