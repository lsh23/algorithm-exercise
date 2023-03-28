from collections import deque


class Solution:
    def solve(self, n: int, m: int, p: int, s_i: list[int], board: list[list[str]]):
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        # for b in board:
        #     print(b)
        q_i = [deque() for _ in range(p + 1)]

        for i in range(n):
            for j in range(m):
                if board[i][j] != "#" and board[i][j] != ".":
                    q_i[int(board[i][j])].append((i, j, 0))



        # 플레이어 i의 성 확장
        # 현재 플레이어 i의 모든 성을 큐에 넣고 BFS
        i = 1
        while True:
            if i == p + 1:
                i = 1

            q: deque = deque(q_i[i])
            q_i[i].clear()
            step = s_i[i]
            while q:
                y, x, l = q.popleft()
                if l == step:
                    q_i[i].append((y, x, 0))
                    continue
                for k in range(4):
                    next_y = y + dy[k]
                    next_x = x + dx[k]
                    if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                        continue
                    if board[next_y][next_x] == '#':  # 벽
                        continue
                    if board[next_y][next_x] != '.':  # 성
                        continue
                    board[next_y][next_x] = str(i)
                    q.append((next_y, next_x, l+1))

            # for q in q_i:
            #     print(q)

            # 게임 종료 확인
            # 모든 플레이어가 더 이상 확장을 할 수 없을 떄
            if all([len(x) == 0 for x in q_i]):
                break

            i += 1

        # for b in board:
        #     print(b)

        s_i_cnt: list[int] = [0] * (p + 1)
        for i in range(n):
            for j in range(m):
                if board[i][j] != "#" and board[i][j] != ".":
                    s_i_cnt[int(board[i][j])] += 1

        for i in range(1, p + 1):
            print(s_i_cnt[i], end=' ')


if __name__ == '__main__':
    N: int
    M: int
    P: int
    S_i: list[int] = [0]
    board: list[list[str]]
    N, M, P = map(int, input().split())
    S_i += [int(x) for x in input().split()]
    assert len(S_i) == P + 1
    board = [[x for x in input()] for _ in range(N)]
    assert len(board) == N and len(board[0]) == M
    s: Solution = Solution()
    s.solve(N, M, P, S_i, board)
