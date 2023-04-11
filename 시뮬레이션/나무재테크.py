from collections import deque


class Tree:
    def __init__(self, x, y, age):
        self.r: int = x
        self.c: int = y
        self.age: int = age
        self.alive: bool = True

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f'r:{self.r} c:{self.c} age:{self.age} alive:{self.alive}'

    def __repr__(self):
        return f'r:{self.r} c:{self.c} age:{self.age} alive:{self.alive}'


class Solution:

    @staticmethod
    def solve(n: int, m: int, k: int, A_r_c: list[list[int]], tree_info: list[list[int]]) -> int:

        dr = [0, -1, 0, 1, 1, -1, -1, 1]
        dc = [1, 0, -1, 0, 1, -1, 1, -1]

        # 처음 땅의 모든 칸의 양분은 5
        map_info: list[list[int]] = [[5] * (n + 1) for _ in range(n + 1)]
        tree: deque[Tree] = deque([Tree(x[0], x[1], x[2]) for x in tree_info])

        # k년 나무 번식 과정 진행
        for _ in range(k):

            # 봄
            # 나무는 자신의 나이 만큼 양분을 먹고, 나이가 1 증가, 같은 칸에 있는 경우 나이 어린 나무가 먼저 먹음
            # 땅에 양분이 부족해서 자신 나의 만큼 먹지 못하면 즉시 죽는다
            dead_tree: list[Tree] = []
            breed_tree: list[Tree] = []

            for _ in range(len(tree)):
                t = tree.popleft()
                age = t.age
                if age <= map_info[t.r][t.c]:
                    map_info[t.r][t.c] -= age
                    t.age += 1
                    if t.age % 5 == 0:
                        breed_tree.append(t)
                else:
                    dead_tree.append(t)
                    continue
                tree.append(t)

            # 여름
            # 봄에서 죽은 나무가 양분으로 변함 죽은 나무의 나이 // 2 가 죽은 나무가 위치하던 칸에 양분으로 추가 된다.
            for t in dead_tree:
                map_info[t.r][t.c] += (t.age // 2)

            # 가을
            # 나무 번식 나무의 나이가 5의 배수인 경우, 인접한 8칸에 대해 나이가 1인 나무 번식
            for t in breed_tree:
                for i in range(8):
                    nr = t.r + dr[i]
                    nc = t.c + dc[i]
                    if nr < 1 or nr > n or nc < 1 or nc > n:
                        continue
                    tree.appendleft(Tree(nr, nc, 1))

            # 겨울
            # 모든 땅에 양분 추가 A_r_c 정보에 맞게 N^2
            for i in range(n):
                for j in range(n):
                    map_info[i + 1][j + 1] += A_r_c[i][j]

        # 살아있는 나무의 수 구하기
        return len(tree)

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    N: int
    M: int
    K: int
    A_r_c: list[list[int]]
    tree_info: list[list[int]]
    N, M, K = map(int, input().split())
    A_r_c = [[int(x) for x in input().split()] for _ in range(N)]
    tree_info = [[int(x) for x in input().split()] for _ in range(M)]
    print(Solution.solve(N, M, K, A_r_c, tree_info))
