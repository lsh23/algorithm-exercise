class Solution:
    @staticmethod
    def solve(n: int, cards: list[int], m: int, targets: list[int]) -> None:
        cnt_dict: dict[int, int] = {}
        for card in cards:
            if card in cnt_dict:
                cnt_dict[card] += 1
            else:
                cnt_dict[card] = 1
        for target in targets:
            if target in cnt_dict:
                print(cnt_dict[target], end=" ")
            else:
                print(0, end=" ")


if __name__ == "__main__":
    N: int
    cards: list[int]
    M: int
    targets: list[int]
    N = int(input())
    cards = [int(x) for x in input().split()]
    M = int(input())
    targets = [int(x) for x in input().split()]
    Solution.solve(N, cards, M, targets)
