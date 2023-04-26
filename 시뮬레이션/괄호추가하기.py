def calculate(operand_1: int, operand_2: int, operator: str) -> int:
    if operator == '+':
        return operand_1 + operand_2
    if operator == '-':
        return operand_1 - operand_2
    if operator == '*':
        return operand_1 * operand_2


class Solution:
    @staticmethod
    def solve(n: int, expr: str) -> int:

        max_result: int = -5000000000

        def dfs(idx: int, result: int):

            nonlocal max_result
            if idx >= len(expr):
                max_result = max(result, max_result)
                return
            operator = expr[idx - 1] if idx > 0 else '+'

            dfs(idx + 2, calculate(result, int(expr[idx]), operator))

            if idx < len(expr) - 2:
                tmp_result = calculate(int(expr[idx]), int(expr[idx + 2]), expr[idx + 1])
                dfs(idx + 4, calculate(result, tmp_result, operator))

        dfs(0, 0)
        return max_result


if __name__ == "__main__":
    N: int
    expression: str
    N = int(input())
    expression = input()
    print(Solution.solve(N, expression))
