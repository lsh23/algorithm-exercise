from collections import deque


class Solution:
    def solve(self, N:int, M:int, targets:list[int]) -> int:
        cnt: int = 0
        dq: deque[int] = deque(range(1,N+1))
        for target in targets:
            tmp_cnt = 0

            while dq[0] != target:
                tmp = dq.popleft()
                dq.append(tmp)
                tmp_cnt += 1
            if tmp_cnt <= (len(dq) // 2):
                cnt += tmp_cnt
            else:
                cnt += len(dq) - tmp_cnt
            dq.popleft()

        return cnt


if __name__ == "__main__":
    N: int
    M: int
    N, M = map(int, input().split())
    targets: list[int] = [ int(x) for x in input().split() ]
    s = Solution()
    print(s.solve(N,M, targets))
