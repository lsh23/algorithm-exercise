class Solution:
    @staticmethod
    def solve(n: int, words: list[str]):
        s: str = ""
        t: str = ""
        max_prefix_len: int = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                word_1 = words[i]
                word_2 = words[j]
                cnt: int = 0
                for k in range(min(len(word_1), len(word_2))):
                    if word_1[k] != word_2[k]:
                        break
                    cnt += 1
                if cnt > max_prefix_len:
                    max_prefix_len = cnt
                    s = word_1
                    t = word_2
        print(s)
        print(t)


if __name__ == "__main__":
    N: int
    words: list[str]
    N = int(input())
    words = [input() for _ in range(N)]
    Solution.solve(N, words)
