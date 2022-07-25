import sys
from typing import List
class Solution:
    def solve(self, statement: str) -> str:

        st: List[str] = []
        for c in statement:
            if c == "(" or c == "[":
                st.append(c)
            if c == ")":
                if len(st) == 0:
                    return "no"
                while st:
                    if st[-1] == "[":
                        return "no"
                    if st[-1] == "(":
                        st.pop()
                        break
                    st.pop()
            if c == "]":
                if len(st) == 0:
                    return "no"
                while st:
                    if st[-1] == "(":
                        return "no"
                    if st[-1] == "[":
                        st.pop()
                        break
                    st.pop()
        if st:
            return "no"
        return "yes"
if __name__ == '__main__':
    input = sys.stdin.readline
    s: Solution = Solution()
    while True:
        statement: str = input().rstrip()
        if statement == ".":
            break
        print(s.solve(statement))
