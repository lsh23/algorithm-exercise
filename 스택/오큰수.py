from typing import List
class Solution:
    def solve(self, N:int, sequence: List[int]) -> None:

        answer: List[int] = []

        nge_on_top: List[int] = []
        for i in range(N-1,-1,-1):
            cur = sequence.pop()
            while True:
                if not nge_on_top:
                    answer.append(-1)
                    break
                nge = nge_on_top[-1]
                if nge > cur:
                    answer.append(nge)
                    break
                nge_on_top.pop()
            nge_on_top.append(cur)
            # nge_on_top 이 비어있으면 -1
            # top이 cur 보다 크면 출력
            # 작으면 pop

        # print(answer)
        for i in range(N-1,-1,-1):
            print(answer[i], end=' ')



if __name__ == '__main__':
    N :int = int(input())
    sequence: List[int] = [int(x) for x in input().split()]
    s :Solution = Solution()
    s.solve(N, sequence)