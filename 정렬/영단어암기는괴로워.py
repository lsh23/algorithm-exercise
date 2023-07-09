class Solution:
    @staticmethod
    def solve(n: int, m: int, words: list[str]) -> None:
        cnt_dict = {}
        for word in words:
            if len(word) < m:
                continue
            if word in cnt_dict:
                cnt_dict[word] += 1
            else:
                cnt_dict[word] = 1

        result: list[tuple[int, str]] = [(cnt_dict[word], word) for word in cnt_dict]
        result.sort(key=lambda x: (-x[0], -len(x[1]), x[1]))
        for x in result:
            print(x[1])


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    N: int
    M: int
    words: list[str]
    N, M = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    Solution.solve(N, M, words)
