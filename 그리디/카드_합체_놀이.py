from typing import List
class Solution:
    def solve(self, n:int, m:int, cards:List[int] ) -> int:

        for _ in range(m):
            cards.sort()
            card_1 = cards[0]
            card_2 = cards[1]
            card_sum = card_1 + card_2
            cards[0] = card_sum
            cards[1] = card_sum

        return sum(cards)

if __name__ == '__main__':

    n,m = map(int,input().split())
    cards = [ int(x) for x in input().split()]
    s :Solution = Solution()
    answer :int = s.solve(n,m,cards)
    print(answer)