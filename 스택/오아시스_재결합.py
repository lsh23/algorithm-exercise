import sys
from typing import List
class Pair:
    def __init__(self, h:int, c:int):
        self.height = h
        self.count = c
    def __str__(self):
        return f'{self.height},{self.count}'
    def __repr__(self):
        return self.__str__()

class Solution:
    def solve(self, q:List[int] ) -> int:
        answer = 0
        st: List[Pair] = []
        for h in q:
            # 스택이 비어있으면 그냥 넣는다
            if not st:
                st.append(Pair(h, 1))
                continue
            # 비어있지 않으면

            c = 1
            if st[-1].height <= h:
                # 스택의 탑이 입력 보다 작거나 같을때
                # 스택의 탑이 입력 보다 작거나 같을때 까지
                # 스택의 탑이 입력과 같을 때
                # 스택의 탑의 원소의 갯수만큼 answer를 더한다.
                # 스택의 탑의 원소의 갯수를 하나
                # 스택의 탑이 입력보다 작을 때
                # 스택에서 원소를 꺼내고 꺼내진 원소의 갯수만큼 answer에 더한다
                # 스택에 입력을 넣는다

                while st and st[-1].height <= h:
                    if st[-1].height == h:
                        answer += st[-1].count
                        c = st[-1].count + 1
                        st.pop()
                    else:
                        answer += st[-1].count
                        st.pop()
                if st:
                    answer += 1
                st.append(Pair(h, c))
            else:
                # 스텍의 탑이 입력 보다 클 때
                # 스택에 입력을 넣는다
                st.append(Pair(h, 1))
                answer += 1
        return answer

if __name__ == '__main__':
    input = sys.stdin.readline
    N:int = int(input())
    q = []
    for _ in range(N):
        q.append(int(input()))
    s = Solution()
    print(s.solve(q))
