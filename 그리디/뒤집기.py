class Solution:
    def solve(self, S:str ) -> int:

        cnt_0: int = 0
        cnt_1: int = 0
        tmp:chr=  ''

        for s in S:
            if tmp != s:
                tmp = s
                if s == '0':
                    cnt_0 += 1
                if s == '1':
                    cnt_1 += 1

        return min(cnt_0,cnt_1)

if __name__ == '__main__':

    S: str = input()
    s :Solution = Solution()
    answer :int = s.solve(S)
    print(answer)