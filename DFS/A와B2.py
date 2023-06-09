class Solution:
    @staticmethod
    def solve(S: str, T: str) -> int:
        t_len: int = len(T)

        answer: int = 0

        def dfs(s: str):
            nonlocal answer
            if len(s) == t_len:
                if s == T:
                    answer = 1
            else:
                next_1 = s + "A"
                next_2 = "B" + s[::-1]
                if T.find(next_1) != -1 or T.find(next_1[::-1]) != -1:
                    dfs(next_1)
                if T.find(next_2) != -1 or T.find(next_2[::-1]) != -1:
                    dfs(next_2)

        dfs(S)

        return answer


if __name__ == "__main__":
    S: str
    T: str
    S = input()
    T = input()
    print(Solution.solve(S, T))
