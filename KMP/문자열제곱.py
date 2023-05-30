class Solution:
    @staticmethod
    def solve(s: str) -> int:
        n: int = len(s)

        j: int = 0
        f: list[int] = [0] * n

        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = f[j - 1]
            if s[i] == s[j]:
                f[i] = j + 1
                j += 1

        if n % (n - f[n - 1]) != 0:
            return 1
        else:
            return n // (n - f[n - 1])

        return answer


if __name__ == "__main__":
    while True:
        s: str
        s = input()
        if s == ".":
            break
        print(Solution.solve(s))
