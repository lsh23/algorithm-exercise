class Solution:
    @staticmethod
    def solve(l: int, s: str) -> int:
        f: list[int] = [0] * l
        j: int = 0
        for i in range(1, l):
            while j > 0 and s[i] != s[j]:
                j = f[j - 1]
            if s[i] == s[j]:
                f[i] = j + 1
                j += 1

        return l - f[l-1]


if __name__ == "__main__":
    L: int
    S: str
    L = int(input())
    S = input()
    print(Solution.solve(L, S))
