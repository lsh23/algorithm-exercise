from typing import List
class Solution:
    def solve(self, bracket_expr) -> int:
        st:List[str] = []
        if len(bracket_expr) % 2 != 0:
            return 0
        for bracket in bracket_expr:
            if bracket == "[":
                st.append(bracket)
            if bracket == "(":
                st.append(bracket)
            if bracket == "]":
                if len(st) == 0:
                    return 0
                tmp = 0
                while st and st[-1] != "[":
                    if st[-1] == "(":
                        return 0
                    tmp += int(st.pop())
                if st:
                    st.pop()
                    if tmp == 0:
                        st.append(3)
                    else:
                        st.append(3*tmp)
                else:
                    return 0
            if bracket == ")":
                if len(st) == 0:
                    return 0
                tmp = 0
                while st and st[-1] != "(":
                    if st[-1] == "[":
                        return 0
                    tmp += int(st.pop())
                if st:
                    st.pop()
                    if tmp == 0:
                        st.append(2)
                    else:
                        st.append(2*tmp)
                else:
                    return 0
        for x in st:
            if x == "[" or x == "(":
                return 0

        return sum(st)
if __name__ == '__main__':
    bracket_expr: str
    bracket_expr = input()
    s :Solution = Solution()
    print(s.solve(bracket_expr))