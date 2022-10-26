from typing import List
class Solution:
    def solve(self, K:int, N:int, cables:List[int]) -> int:

        l: int = 1
        r: int = max(cables)

        ans: int = 0

        i = 0
        while l<=r:
            mid: int = (l+r) // 2
            cnt: int = 0
            for cable in cables:
                cnt += (cable // mid)
            if cnt < N:
                r = mid-1
            else:
                l = mid+1
                ans = max(ans,mid)

        return ans

if __name__ == '__main__':
    K: int
    N: int
    K,N = map(int,input().split())
    cables: List[int] = [ int(input()) for _ in range(K)]
    s :Solution = Solution()
    print(s.solve(K,N,cables))
