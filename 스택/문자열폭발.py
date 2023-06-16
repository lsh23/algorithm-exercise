class Solution:
    @staticmethod
    def solve(s1: str, s2: str) -> str:
        answer: str = "FRULA"

        st: list[str] = []
        for c in s1:
            st.append(c)
            if len(st) >= len(s2):
                if "".join(st[-(len(s2)):]) == s2:
                    for _ in range(len(s2)):
                        st.pop()

        if len(st) != 0:
            answer = "".join(st)

        return answer


if __name__ == "__main__":
    s1: str
    s2: str
    s1 = input()
    s2 = input()
    print(Solution.solve(s1, s2))
