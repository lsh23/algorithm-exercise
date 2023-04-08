from itertools import permutations


class Solution:
    @staticmethod
    def solve(n: int, ai: list[int], op_info: list[int]) -> int:
        max_ans: int = -1000000001
        min_ans: int = 1000000001

        operations = []
        for i in range(4):
            op_cnt = op_info[i]
            operations += [i] * op_cnt

        for op_order in permutations(operations):
            result: int = ai[0]
            for i in range(n - 1):
                if op_order[i] == 0:
                    result = result + ai[i + 1]
                if op_order[i] == 1:
                    result = result - ai[i + 1]
                if op_order[i] == 2:
                    result = result * ai[i + 1]
                if op_order[i] == 3:
                    if result < 0 and ai[i + 1] > 0:
                        result = -1*(-result // ai[i + 1])
                    else:
                        result = result // ai[i + 1]

            max_ans = max(result, max_ans)
            min_ans = min(result, min_ans)

        print(max_ans)
        print(min_ans)


if __name__ == "__main__":
    N: int
    Ai: list[int]
    operation_info: list[int]

    N = int(input())
    Ai = [int(x) for x in input().split()]
    operation_info = [int(x) for x in input().split()]
    Solution.solve(N, Ai, operation_info)
