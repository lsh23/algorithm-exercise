dy: list[int] = [0, -1, 1, 0, 0]
dx: list[int] = [0, 0, 0, 1, -1]


class Shark:
    pass


class Shark:
    def __init__(self, r: int, c: int, s: int, d: int, z: int):
        self.r = r
        self.c = c
        self.s = s
        self.d = d
        self.z = z

    def move(self, map_info: list[list[list[Shark]]]):
        map_info[self.r][self.c].remove(self)

        nr: int = self.r
        nc: int = self.c

        if self.d == 1 or self.d == 2:
            s = self.s % (2 * R - 2)
        else:
            s = self.s % (2 * C - 2)

        for i in range(s):
            if nr == 0 and self.d == 1:
                self.d = 2
            if nr == R - 1 and self.d == 2:
                self.d = 1
            if nc == 0 and self.d == 4:
                self.d = 3
            if nc == C - 1 and self.d == 3:
                self.d = 4
            nr = nr + dy[self.d]
            nc = nc + dx[self.d]

        self.r = nr
        self.c = nc

        map_info[self.r][self.c].append(self)

    def __repr__(self):
        return f'({self.s}, {self.z})'


class Solution:
    @staticmethod
    def solve(R: int, C: int, M: int, sharks: list[Shark]):
        answer: int = 0

        map_info: list[list[list[Shark]]] = [[[] for _ in range(C)] for _ in range(R)]

        for s in sharks:
            map_info[s.r][s.c].append(s)
        # print("first")
        # print(*map_info, sep="\n")
        # 낚시왕이 오른쪽으로 한칸 이동한다.
        for fish_king in range(C):
            # 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 잡힌 상어는 사라진다.
            for i in range(R):
                if map_info[i][fish_king]:
                    # print(fish_king, i)
                    fished = map_info[i][fish_king][0]
                    sharks.remove(fished)
                    map_info[i][fish_king].remove(fished)
                    answer += fished.z
                    break

            # print("after fishing")
            # print(*map_info, sep="\n")

            # 상어가 이동한다.
            for s in sharks:
                s.move(map_info)
            # print("after move")
            # print(*map_info, sep="\n")

            # 이동 후, 같은 위치에 있는 경우 가장 큰 상어가 나머지 상어를 잡아 먹는다.
            for i in range(R):
                for j in range(C):
                    if len(map_info[i][j]) > 1:
                        max_shark_i = 0
                        for k in range(len(map_info[i][j])):
                            if map_info[i][j][max_shark_i].z < map_info[i][j][k].z:
                                max_shark_i = k
                        for k in range(len(map_info[i][j])):
                            if k != max_shark_i:
                                sharks.remove(map_info[i][j][k])
                        map_info[i][j] = [map_info[i][j][max_shark_i]]
            # print("after merge")
            # print(*map_info, sep="\n")
            # print("----------")
        return answer


if __name__ == "__main__":
    R: int
    C: int
    M: int
    R, C, M = map(int, input().split())
    sharks: list[Shark] = []
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        sharks.append(Shark(r - 1, c - 1, s, d, z))
    print(Solution.solve(R, C, M, sharks))
