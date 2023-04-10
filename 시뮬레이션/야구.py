from itertools import permutations


class Solution:
    @staticmethod
    def solve(n: int, player_stats: list[int]) -> int:
        ans: int = 0
        # 타순 정하기 - 순열
        player_numbers: list[int] = [i for i in range(1, 9)]
        for players in permutations(player_numbers):
            # 정한 타순대로 경기진행 시 득점 구하기 8!
            players = list(players)
            players = players[:3] + [0] + players[3:]
            score: int = 0
            cur_batter_idx: int = 0
            for inning in range(n):
                out_count: int = 0
                base_1: int = 0
                base_2: int = 0
                base_3: int = 0
                while out_count != 3: ## 한이닝에 최대 22명이 타격할 수 있음
                    result = player_stats[inning][players[cur_batter_idx]]
                    if result == 0:
                        out_count += 1
                    if result == 1:
                        score += base_3
                        base_3 = base_2
                        base_2 = base_1
                        base_1 = 1
                    if result == 2:
                        score += (base_2 + base_3)
                        base_3 = base_1
                        base_1 = 0
                        base_2 = 1
                    if result == 3:
                        score += (base_1 + base_2 + base_3)
                        base_1 = 0
                        base_2 = 0
                        base_3 = 1
                    if result == 4:
                        score += (base_1 + base_2 + base_3) + 1
                        base_1 = 0
                        base_2 = 0
                        base_3 = 0
                    cur_batter_idx = (cur_batter_idx + 1) % 9
            # 최댓값 갱신
            ans = max(score, ans)
        return ans


if __name__ == "__main__":
    N: int
    player_stats: list[int]
    N = int(input())
    player_stats = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, player_stats))
