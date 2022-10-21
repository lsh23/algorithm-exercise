class Solution:
    def solve(self,N: int,r: int,c: int) -> int:

        ans: int = 0
        while N != 0:
            N -= 1

            if r < 2**N and c < 2**N:
                ans += (2**N)*(2**N)*0

            elif r < 2**N and c >= 2**N:
                ans += (2**N)*(2**N)*1
                c -= (2**N)

            elif r >= 2**N and c < 2**N:
                ans += (2**N)*(2**N)*2
                r -= (2**N)
            else:
                ans += (2**N)*(2**N)*3
                c -= (2 ** N)
                r -= (2 ** N)

        return ans

    def solve_recur(self, N: int, r: int, c: int) -> int:
        global ans
        ans = 0
        def recur(N: int,r: int,c: int):
            global ans
            N -= 1
            if N == -1:
                return 0
            if r < 2**N and c < 2**N:
                recur(N,r,c)
            elif r < 2**N and c >= 2**N:
                ans += (2**N)*(2**N)*1
                recur(N, r, c-(2**N))
            elif r >= 2**N and c < 2**N:
                ans += (2**N)*(2**N)*2
                recur(N, r-(2**N), c)
            else:
                ans += (2 ** N) * (2 ** N) * 3
                recur(N, r-(2**N), c-(2**N))
        recur(N,r,c)
        return ans


if __name__ == '__main__':
    N: int
    r: int
    c: int
    N,r,c = map(int,input().split())

    s :Solution = Solution()
    print(s.solve(N,r,c))
    # print(s.solve_recur(N,r,c))