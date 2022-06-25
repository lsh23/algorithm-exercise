from typing import List, Tuple
class Solution:
    def solve(self, N:int, eggs: List[List[int]]) -> int:

        global answer
        answer = 0

        def dfs(l:int):
            global answer
            if l == N:
                cnt = 0
                for egg in eggs:
                    if egg[0] <= 0:
                        cnt+=1
                answer = max(cnt, answer)
            else:
                cur = eggs[l]
                cur_s = cur[0]
                cur_w = cur[1]
                if cur_s <=0:
                    dfs(l+1)
                else:
                    for i in range(N):
                        if i==l:
                            continue
                        egg_i = eggs[i]
                        i_s = egg_i[0]
                        i_w = egg_i[1]
                        if i_s >=1:
                            cur_s -= i_w
                            i_s -= cur_w
                            eggs[l][0] = cur_s
                            eggs[i][0] = i_s
                            dfs(l+1)
                            eggs[i][0] = i_s + cur_w
                            eggs[l][0] = cur_s + i_w
                            i_s += cur_w
                            cur_s += i_w
                        else:
                            dfs(l + 1)

        dfs(0)

        return answer

if __name__ == '__main__':
    N: int = int(input())
    eggs: List[List[int]] = []

    for i in range(N):
        s,w = map(int,input().split())
        eggs.append([s,w])

    s :Solution = Solution()
    answer :int = s.solve(N, eggs)
    print(answer)