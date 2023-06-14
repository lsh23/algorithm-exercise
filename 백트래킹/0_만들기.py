def make_expr(n: int, selected: list[int]):
    expr: str = ""
    for i in range(n - 1):
        op: str = ""
        if selected[i] == 0:
            op = '+'
        elif selected[i] == 1:
            op = '-'
        else:
            op = ' '
        expr += (f'{i + 1}{op}')
    expr += f'{n}'
    return expr


def calculate(expr: str) -> int:
    prev_op: str = "+"
    prev_idx: int = -1
    result: int = 0
    for i in range(len(expr)):
        if not expr[i].isdigit():
            if prev_op == "+":
                result += int(expr[prev_idx + 1:i])
            else:
                result -= int(expr[prev_idx + 1:i])
            prev_idx = i
            if expr[i] == "+":
                prev_op = "+"
            else:
                prev_op = '-'
    if prev_idx == -1:
        result = int(expr)
    else:
        if prev_op == "+":
            result += int(expr[prev_idx + 1:])
        else:
            result -= int(expr[prev_idx + 1:])
    return result


class Solution:
    @staticmethod
    def solve(n: int):
        answer: list[str] = []

        def make_operator(l: int, selected: list[int]):
            nonlocal answer
            if l == n - 1:
                expr: str = make_expr(n, selected)
                if calculate(expr.replace(' ', '')) == 0:
                    answer.append(expr)
            else:
                for i in range(3):
                    selected[l] = i
                    make_operator(l + 1, selected)

        make_operator(0, [0] * (n - 1))
        answer.sort()
        for x in answer:
            print(x)


if __name__ == "__main__":
    T: int
    T = int(input())
    for _ in range(T):
        N: int = int(input())
        Solution.solve(N)
        print()
