class Solution:
    @staticmethod
    def solve(N: int, numbers: list[int]) -> None:
        zipped: dict[int, int] = {value: idx for idx, value in enumerate(sorted(list(set(numbers))))}
        for x in numbers:
            print(zipped[x], end=" ")


if __name__ == "__main__":
    N: int
    numbers: list[int]
    N = int(input())
    numbers = [int(x) for x in input().split()]
    Solution.solve(N, numbers)
