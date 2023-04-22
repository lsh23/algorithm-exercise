dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]


class Shark:
    pass


class Shark:
    def __init__(self, n: int, y: int, x: int, d: int, d_priority: list[list[int]]):
        self.n: int = n
        self.y: int = y
        self.x: int = x
        self.d: int = d
        self.d_priority: list[list[int]] = d_priority
        self.alive = True

    def move(self, map_smell_info: list[list[list[int]]], after_map_smell_info: list[list[list[int]]],
             map_shark_info: list[list[list[Shark]]]):
        if self.alive is False:
            return
        # 이동 방향 정하는 기준
        # 인접 방향 중 아무 냄새가 없는 칸으로 (우선 순위 적용)
        # print("number", self.n)
        # print(self.d)
        # print(self.d_priority[self.d - 1])
        for i in self.d_priority[self.d - 1]:
            ny = self.y + dy[i]
            nx = self.x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if map_smell_info[ny][nx][1] != 0:
                continue
            self.y = ny
            self.x = nx
            self.d = i
            after_map_smell_info[ny][nx] = [self.n, k]
            map_shark_info[ny][nx].append(self)
            return

        # 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 (우선 순위 적용)
        for i in self.d_priority[self.d - 1]:
            ny = self.y + dy[i]
            nx = self.x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if map_smell_info[ny][nx][0] != self.n:
                continue
            self.y = ny
            self.x = nx
            self.d = i
            after_map_smell_info[ny][nx] = [self.n, k]
            map_shark_info[ny][nx].append(self)
            return

    def __lt__(self, other):
        return self.n < other.n

    def __repr__(self):
        return str(self.n)


class Solution:
    @staticmethod
    def solve(n: int, m: int, k: int, map_info: list[list[int]], shark_direction_info: list[list[int]],
              shark_direction_priority_info: list[list[list[int]]]) -> int:
        map_smell_info: list[list[list[int]]] = [[[0, 0]] * n for _ in range(n)]
        map_shark_info: list[list[list[Shark]]] = [[[] for _ in range(n)] for _ in range(n)]
        sharks: list[Shark] = [None] * (m + 1)

        # 1. 맨 처음에는 모든 상어가 자신의 위치에 냄새를 뿌린다.
        idx: int = 0
        for i in range(n):
            for j in range(n):
                if map_info[i][j] != 0:
                    shark_number: int = map_info[i][j]
                    shark = Shark(shark_number, i, j, shark_direction_info[shark_number],
                                  shark_direction_priority_info[shark_number])
                    sharks[shark_number] = shark
                    map_smell_info[i][j] = [shark_number, k]
                    map_shark_info[i][j].append(shark)
                    idx += 1

        # print("------first-----")
        # print("shark")
        # for _s in map_shark_info:
        #     print(_s)
        # print("smell")
        # for _m in map_smell_info:
        #     print(_m)

        ans: int = 0
        while ans < 1000:
            ans += 1

            # 2. 모든 상어가 1초마다 동시에 인접한 칸 중 하나로 이동하고 자신의 냄새를 그 칸에 뿌린다.
            after_map_shark_info: list[list[list[Shark]]] = [[[] for _ in range(n)] for _ in range(n)]
            after_map_smell_info: list[list[list[int]]] = [[[x for x in y] for y in z] for z in map_smell_info]
            for i in range(1, m + 1):
                shark = sharks[i]
                shark.move(map_smell_info, after_map_smell_info, after_map_shark_info)

            # print("after move---------")
            # print("shark")
            # for _s in after_map_shark_info:
            #     print(_s)

            map_smell_info = after_map_smell_info
            # 모든 상어가 이동 한 후에 한칸에 여러 마리의 상어가 남아있으면 가장 작은 번호를 가진 상어가 나머지를 겪자밖으로 쫓아냄
            for i in range(n):
                for j in range(n):
                    if len(after_map_shark_info[i][j]) > 1:
                        after_map_shark_info[i][j].sort()
                        for x in range(1, len(after_map_shark_info[i][j])):
                            after_map_shark_info[i][j][x].alive = False
                        after_map_shark_info[i][j] = after_map_shark_info[i][j][:1]
                        map_smell_info[i][j] = [after_map_shark_info[i][j][0].n, k]

            map_shark_info = after_map_shark_info

            # 냄새는 상어가 k번 이동하면 사라짐
            for i in range(n):
                for j in range(n):
                    if map_smell_info[i][j][1] != 0 and len(map_shark_info[i][j]) == 0:
                        map_smell_info[i][j] = [map_smell_info[i][j][0], map_smell_info[i][j][1] - 1]

            # print("겹치는 상어 정리 후---------")
            # print("shark")
            # for _s in after_map_shark_info:
            #     print(_s)
            #
            # print("smell")
            # for _m in map_smell_info:
            #     print(_m)

            # 3. 1번 상어만 격자에 남게 되는데 까지 걸리는 시간
            if all([sharks[i].alive == False for i in range(2, m + 1)]):
                return ans

        return -1


if __name__ == "__main__":
    N: int
    M: int
    k: int
    map_info: list[list[int]]
    shark_direction_info: list[list[int]]
    shark_info: list[list[list[int]]]
    N, M, k = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(N)]
    shark_direction_info = [0] + [int(x) for x in input().split()]
    shark_info = [[]] + [[[int(x) for x in input().split()] for _ in range(4)] for _ in range(M)]
    print(Solution.solve(N, M, k, map_info, shark_direction_info, shark_info))
