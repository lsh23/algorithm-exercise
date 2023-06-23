class Solution:
    @staticmethod
    def solve(n: int, k: int, result_info: list[tuple[int, int, int, int]]) -> int:
        result_info.sort()
        k_result = (result_info[k - 1][1], result_info[k - 1][2], result_info[k - 1][3])
        result_cnt: dict[tuple[int, int, int], int] = {}
        for x in result_info:
            number, gold, silver, bronze = x
            result = (gold, silver, bronze)
            if result in result_cnt:
                result_cnt[result] += 1
            else:
                result_cnt[result] = 1

        result_list = [[*result, result_cnt[result]] for result in result_cnt]
        result_list.sort(reverse=True)

        rank: int = 0
        for i in range(n):
            gold, silver, bronze, cnt = result_list[i]
            k_gold, k_silver, k_bronze = k_result
            if gold == k_gold and silver == k_silver and bronze == k_bronze:
                rank += 1
                return rank
            rank += cnt


if __name__ == "__main__":
    N: int
    K: int
    result_info: list[tuple[int, int, int, int]] = []
    N, K = map(int, input().split())
    for _ in range(N):
        result_info.append(tuple(map(int, input().split())))
    print(Solution.solve(N, K, result_info))
