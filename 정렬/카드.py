from __future__ import annotations
import sys

class Card:
    def __init__(self, value: int):
        self.value = value
        self.cnt = 1

    def add_count(self):
        self.cnt += 1

    def __lt__(self, other: Card):
        if self.cnt > other.cnt:
            return True
        elif self.cnt == other.cnt:
            return self.value < other.value
        else:
            return False


    # def __repr__(self):
    #     return f'({self.value}, {self.cnt})'


class Solution:
    def solve(self, n: int, cards: list[int]) -> int:
        dict_card_cnt: dict[int, Card] = {}
        for i in range(N):
            if cards[i] in dict_card_cnt:
                dict_card_cnt[cards[i]].add_count()
            else:
                dict_card_cnt[cards[i]] = Card(cards[i])

        card_cnt_result = dict_card_cnt.values()
        card_cnt_result = list(card_cnt_result)
        card_cnt_result.sort()
        return card_cnt_result[0].value

    def solve2(self, n: int, cards: list[int]) -> int:
        dict_card_cnt: dict[int, int] = {}
        for i in range(N):
            if cards[i] in dict_card_cnt:
                dict_card_cnt[cards[i]] += 1
            else:
                dict_card_cnt[cards[i]] = 1

        a = sorted(dict_card_cnt.items(), key=lambda x: (-x[1], x[0]))
        return a[0][0]

if __name__ == '__main__':
    input = sys.stdin.readline
    N: int = int(input())
    cards = [ int(input()) for _ in range(N) ]
    s :Solution = Solution()
    print(s.solve(N, cards))