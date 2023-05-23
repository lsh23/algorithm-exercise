class Solution:
    @staticmethod
    def solve(s: str, p: str):
        n = len(p)
        f: list[int] = [0] * n
        j: int = 0

        for i in range(1, n):
            while j > 0 and p[i] != p[j]:
                j = f[j - 1]
            if p[i] == p[j]:
                f[i] = j + 1
                j += 1

        j = 0
        for i in range(0, len(s)):
            while j > 0 and s[i] != p[j]:
                j = f[j - 1]
            if s[i] == p[j]:
                j += 1
            if j == n:
                return 1

        return 0


if __name__ == "__main__":
    S: str
    P: str
    S = input()
    P = input()
    print(Solution.solve(S, P))
