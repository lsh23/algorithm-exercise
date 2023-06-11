def check(n: int, cur: int, numbers: list[int], selected: list[int], checked: list[int]) -> bool:
    if n == numbers[cur]:
        selected[n] = 1
        # print(selected)
        for i in range(1, n + 1):
            if selected[i]:
                checked[i] = 1
    else:
        k = numbers[cur]
        if selected[k] == 0:
            selected[k] = 1
            check(n, k, numbers, selected, checked)
            selected[k] = 0


class Solution:
    @staticmethod
    def solve(n: int, numbers: list[int]) -> None:
        checked: list[int] = [0] * (n + 1)
        for i in range(1, n + 1):
            if checked[i] != 0:
                continue
            check(i, i, numbers, [0] * (n + 1), checked)

        print(sum(checked))
        for i in range(1, n + 1):
            if checked[i] == 1:
                print(i)


if __name__ == "__main__":
    N: int
    numbers: list[int]
    N = int(input())
    numbers = [0] * (N + 1)
    for i in range(1, N + 1):
        numbers[i] = int(input())
    Solution.solve(N, numbers)
