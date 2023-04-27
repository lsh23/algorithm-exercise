def check_end_game(play_board: list[list[int]]) -> bool:
    enemy_cnt: int = 0
    for i in range(N):
        for j in range(M):
            if play_board[i][j] != 0:
                enemy_cnt += 1
    return enemy_cnt == 0


def move_enemy(play_board: list[list[int]]) -> list[list[int]]:
    next_play_board = [[0] * M for _ in range(N)]
    for i in range(1, N):
        next_play_board[i] = play_board[i - 1]
    return next_play_board


def choose_targets(enemies: list[int], selected_archer: list[int]) -> list[int]:
    targets: list[int] = []
    for archer in selected_archer:
        a_y = N
        a_x = archer
        min_dist: int = 31
        min_e_x = M
        target = -1
        for i in range(len(enemies)):
            e_y, e_x = enemies[i]
            dist = abs(a_y - e_y) + abs(a_x - e_x)
            if dist > D:
                continue
            if dist < min_dist:
                min_dist = dist
                target = i
                min_e_x = e_x
            if dist == min_dist:
                if e_x < min_e_x:
                    target = i
                    min_e_x = e_x
        if target != -1:
            if all([x != target for x in targets]):
                targets.append(target)
    return targets


class Solution:
    @staticmethod
    def solve(n: int, m: int, d: int, board: list[list[int]]) -> int:

        ans: int = 0
        # 1. N+1의 행의 M개의 열중 3개를 골라서 궁수를 배치한다 O(mC3)
        selected_archer = [0] * 3

        def select_archer(k: int, l: int):
            nonlocal ans
            if l == 3:
                cnt: int = 0
                play_board: list[list[int]] = [[x for x in y] for y in board]

                while True:
                    # 1. 현재 격자판에 있는 적의 정보
                    enemies: list[tuple[int, int]] = []
                    for i in range(n):
                        for j in range(m):
                            if play_board[i][j] != 0:
                                enemies.append((i, j))

                    # 2. 각 궁수마다 공격할 적을 선택하고 공격한다 O(NM)
                    targets: list[int] = choose_targets(enemies, selected_archer)
                    for target in targets:
                        t_y, t_x = enemies[target]
                        play_board[t_y][t_x] = 0
                    cnt += len(targets)

                    # 3. 적들이 한칸 아래로 전부 이동한다.
                    play_board = move_enemy(play_board)

                    # 모든적이 격자판에서 제외되면 게임은 종료된다.
                    if check_end_game(play_board) is True:
                        break

                # 궁수의 공격으로 제거할 수 이는 적의 최대 수
                ans = max(cnt, ans)
                return
            else:
                for i in range(k, m):
                    selected_archer[l] = i
                    select_archer(i + 1, l + 1)

        select_archer(0, 0)

        return ans


if __name__ == "__main__":
    N: int
    M: int
    D: int
    board: list[list[int]]
    N, M, D = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, M, D, board))
