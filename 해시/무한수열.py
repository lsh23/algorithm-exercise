import sys
class Solution:
    def solve(self, N:int, P:int, Q:int) -> int:

        cache = dict()
        cache[0] = 1
        def dp(k):
            if k==0:
                return 1
            else:
                if k in cache.keys():
                    return cache[k]
                else:
                    cache[k] = dp(k//P) + dp(k//Q)
                    return cache[k]
        return dp(N)

if __name__ == '__main__':
    input = sys.stdin.readline
    N: int
    P: int
    Q: int
    N,P,Q = map(int, input().split())
    s :Solution = Solution()
    print(s.solve(N,P,Q))
