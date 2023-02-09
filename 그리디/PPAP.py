class Solution:
    def solve(self,string: str) -> str:

        # 스택에 하나씩 넣고
        # 스택의 길이가 4이상이면서 탑부터 탑-3이 PPAP면 pop하고 P를 넣는다.

        st: list[str] = []
        for c in string:
            st.append(c)
            if len(st) >= 4 and "".join(st[-4:]) == "PPAP":
                st.pop()
                st.pop()
                st.pop()

        if "".join(st) == "P":
            return "PPAP"
        return "NP"


if __name__ == '__main__':
    string: str = input()
    s :Solution = Solution()
    print(s.solve(string))