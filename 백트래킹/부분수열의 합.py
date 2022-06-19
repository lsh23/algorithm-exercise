from typing import List
class Solution:
    def solve(self, N:int, S:int, sequence:List[int] ) -> int:
        global cnt
        cnt = 0
        selected: List[int] = [0]*N

        def dfs(k:int):
            global cnt
            if k==N:
                subsequence_sum: int = 0
                if sum(selected) > 0:
                    for i in range(N):
                        if selected[i]==1:
                            subsequence_sum+=sequence[i]
                    if subsequence_sum == S:
                        # print(selected)
                        cnt += 1
            else:
                selected[k]=1
                dfs(k+1)
                selected[k]=0
                dfs(k+1)

        dfs(0)
        return cnt

if __name__ == '__main__':
    N :int
    S :int
    N,S = map(int,input().split())
    sequence: List[int] = [int(x) for x in input().split()]
    s :Solution = Solution()
    answer :int = s.solve(N,S, sequence)
    print(answer)