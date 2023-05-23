class Solution:
    @staticmethod
    def solve(s: str, k: str) -> int:
        s = [x for x in s if not ord('0') <= ord(x) <= ord('9')]
        s = "".join(s)

        f: list[int] = [0] * len(k)
        j = 0
        for i in range(1, len(k)):
            while j > 0 and k[i] != k[j]:
                j = f[j - 1]
            if k[i] == k[j]:
                f[i] = j + 1
                j += 1

        j = 0
        for i in range(0, len(s)):
            while j > 0 and s[i] != k[j]:
                j = f[j - 1]
            if s[i] == k[j]:
                j += 1
            if j == len(k):
                return 1

        return 0


if __name__ == "__main__":
    S: str
    K: str
    S = input()
    K = input()
    print(Solution.solve(S, K))
