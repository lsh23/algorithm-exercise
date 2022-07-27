from typing import List
class Solution:
    def solve(self, word:str) -> int:
        st: List[str] = []
        if len(word) % 2 != 0:
            return 0
        for c in word:
            if c == "A":
                if st and st[-1] == "A":
                        st.pop()
                else:
                    st.append(c)
            if c == "B":
                if st and st[-1] == "B":
                    st.pop()
                else:
                    st.append(c)
        if st:
            return 0
        else:
            return 1

if __name__ == '__main__':
    N: int = int(input())
    s: Solution = Solution()
    ans: int = 0
    for _ in range(N):
        word: str = input()
        ans += s.solve(word)
    print(ans)