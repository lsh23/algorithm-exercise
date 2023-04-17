from itertools import permutations

JIWOO = 1
GYEONGHEE = 2
MINHO = 3


class Solution:
    @staticmethod
    def solve(n: int, k: int, a_i_j: list[list[int]], gh_order: list[int], mh_order: list[int]) -> int:

        ans: int = 0
        for JW in permutations([i for i in range(n)]):
            if ans == 1:
                break
            win_cnt: dict[int, int] = {}
            hand_shape: dict[int, list[int]] = {}
            participation_cnt: dict[int, int] = {}

            win_cnt[JIWOO] = 0
            win_cnt[GYEONGHEE] = 0
            win_cnt[MINHO] = 0

            hand_shape[JIWOO] = JW
            hand_shape[GYEONGHEE] = gh_order
            hand_shape[MINHO] = mh_order

            participation_cnt[JIWOO] = 0
            participation_cnt[GYEONGHEE] = 0
            participation_cnt[MINHO] = 0

            p1: int
            p2: int
            p3: int
            p1 = JIWOO
            p2 = GYEONGHEE
            p3 = MINHO

            while True:
                if win_cnt[JIWOO] == k:
                    ans = 1
                    break
                if win_cnt[GYEONGHEE] == k or win_cnt[MINHO] == k:
                    break
                if participation_cnt[JIWOO] >= n:
                    break
                if participation_cnt[GYEONGHEE] >= 20 or participation_cnt[MINHO] >= 20:
                    break

                hand_shape_p1 = hand_shape[p1][participation_cnt[p1]]
                hand_shape_p2 = hand_shape[p2][participation_cnt[p2]]
                participation_cnt[p1] += 1
                participation_cnt[p2] += 1

                if a_i_j[hand_shape_p1][hand_shape_p2] == 2:
                    win_cnt[p1] += 1
                    p2, p3 = p3, p2
                elif a_i_j[hand_shape_p1][hand_shape_p2] == 1:
                    if p2 > p1:
                        win_cnt[p2] += 1
                        p1, p3 = p3, p1
                    else:
                        win_cnt[p1] += 1
                        p2, p3 = p3, p2
                else:
                    win_cnt[p2] += 1
                    p1, p3 = p3, p1
        return ans


if __name__ == "__main__":
    N: int
    K: int
    A_i_j: list[list[int]]
    gh_order: list[int]
    mh_order: list[int]
    N, K = map(int, input().split())
    A_i_j = [[int(x) for x in input().split()] for _ in range(N)]
    gh_order = [int(x) - 1 for x in input().split()]
    mh_order = [int(x) - 1 for x in input().split()]
    print(Solution.solve(N, K, A_i_j, gh_order, mh_order))
