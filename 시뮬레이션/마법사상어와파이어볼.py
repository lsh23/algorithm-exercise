dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


class FireBall:
    def __init__(self, r: int, c: int, m: int, s: int, d: int):
        self.r: int = r
        self.c: int = c
        self.m: int = m
        self.s: int = s
        self.d: int = d

    def move(self):
        nr = (self.r + (dr[self.d] * self.s)) % N
        nc = (self.c + (dc[self.d] * self.s)) % N

        self.r = nr
        self.c = nc

        return nr, nc

    def __repr__(self):
        return f'{self.r},{self.c},{self.m},{self.s},{self.d}'


class Solution:
    @staticmethod
    def solve(n: int, m: int, k: int, fireball_info: list[FireBall]) -> int:

        board: list[list[list[FireBall]]] = [[[] for _ in range(n)] for _ in range(n)]

        for fireball in fireball_info:
            board[fireball.r][fireball.c].append(fireball)

        # k번 반복
        for _ in range(k):
            # 1. 파이어볼 이동
            board = [[[] for _ in range(n)] for _ in range(n)]
            for fireball in fireball_info:
                r, c = fireball.move()
                board[r][c].append(fireball)

            # 2. 파이어볼이 2개 이상이 있는 칸
            for i in range(n):
                for j in range(n):
                    if len(board[i][j]) >= 2:
                        s_sum: int = 0
                        m_sum: int = 0
                        odd_d_cnt: int = 0
                        even_d_cnt: int = 0
                        cnt: int = 0
                        for f in board[i][j]:
                            cnt += 1
                            s_sum += f.s
                            m_sum += f.m
                            if f.d % 2 == 0:
                                even_d_cnt += 1
                            else:
                                odd_d_cnt += 1
                            fireball_info.remove(f)

                        board[i][j] = []

                        if m_sum // 5 == 0:
                            continue

                        if even_d_cnt == 0 or odd_d_cnt == 0:
                            board[i][j].append(FireBall(i, j, m_sum // 5, s_sum // cnt, 0))
                            board[i][j].append(FireBall(i, j, m_sum // 5, s_sum // cnt, 2))
                            board[i][j].append(FireBall(i, j, m_sum // 5, s_sum // cnt, 4))
                            board[i][j].append(FireBall(i, j, m_sum // 5, s_sum // cnt, 6))
                        else:
                            board[i][j].append(FireBall(i, j, m_sum // 5, s_sum // cnt, 1))
                            board[i][j].append(FireBall(i, j, m_sum // 5, s_sum // cnt, 3))
                            board[i][j].append(FireBall(i, j, m_sum // 5, s_sum // cnt, 5))
                            board[i][j].append(FireBall(i, j, m_sum // 5, s_sum // cnt, 7))

                        for f in board[i][j]:
                            fireball_info.append(f)

        ans: int = 0
        for i in range(n):
            for j in range(n):
                for f in board[i][j]:
                    ans += f.m
        return ans


if __name__ == "__main__":
    N: int
    M: int
    K: int
    fireball_info: list[FireBall] = []
    N, M, K = map(int, input().split())
    for i in range(M):
        r, c, m, s, d = map(int, input().split())
        fireball_info.append(FireBall(r - 1, c - 1, m, s, d))

    print(Solution.solve(N, M, K, fireball_info))
