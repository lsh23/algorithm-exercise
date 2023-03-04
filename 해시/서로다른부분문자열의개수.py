class Solution:
    def solve(self, S: str) -> int:
        sub: dict = {}

        for i in range(len(S)):
            for j in range(i, len(S)):
                if not S[i:j+1] in sub:
                    sub[S[i:j+1]] = 1

        return len(sub.values())


if __name__ == '__main__':
    S: str = input()
    s: Solution = Solution()
    print(s.solve(S))