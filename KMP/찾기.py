class Solution:
    @staticmethod
    def solve(t: str, p: str) -> None:
        f: list[int] = [0] * len(p)
        j: int = 0
        for i in range(1, len(p)):
            while j > 0 and p[i] != p[j]:
                j = f[j - 1]
            if p[i] == p[j]:
                f[i] = j + 1
                j += 1
        ans: list[int] = []
        j = 0
        for i in range(len(t)):
            while j > 0 and t[i] != p[j]:
                j = f[j - 1]
            if t[i] == p[j]:
                j += 1
            if j == len(p):
                ans.append(i - len(p) + 1 + 1)
                j = f[j - 1]

        print(len(ans))
        print(*ans, sep=" ")


if __name__ == "__main__":
    T: str
    P: str
    T = input()
    P = input()
    Solution.solve(T, P)
