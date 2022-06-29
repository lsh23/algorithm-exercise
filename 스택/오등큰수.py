from typing import List
class Solution:
    def solve(self, N:int, sequence: List[int]) -> None:


        cnt: List[int] = [0]*(1000001)

        for x in sequence:
            cnt[x]+=1

        answer: List[int] = [0]*(1000001)

        ngf_on_top: List[int] = []
        for i in range(N-1,-1,-1):
            cur = sequence.pop()
            while True:
                if not ngf_on_top:
                    answer[i]=-1
                    break
                ngf = ngf_on_top[-1]
                if cnt[ngf] > cnt[cur]:
                    answer[i]=ngf
                    break
                ngf_on_top.pop()
            ngf_on_top.append(cur)

        # print(answer)
        for i in range(0,N):
            print(answer[i], end=' ')


if __name__ == '__main__':
    N :int = int(input())
    sequence: List[int] = [int(x) for x in input().split()]
    s :Solution = Solution()
    s.solve(N, sequence)