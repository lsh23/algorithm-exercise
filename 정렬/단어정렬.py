import sys


class Solution:
    def solve(self, n: int, words: list[str]) -> None:
        set_words: set[str] = set(words)
        result_words = sorted(list(set_words), key=lambda x:(len(x),x))
        for word in result_words:
            print(word)


if __name__ == '__main__':
    input = sys.stdin.readline
    N: int = int(input())
    a : str
    words = [ input().strip() for _ in range(N) ]
    s :Solution = Solution()
    s.solve(N, words)