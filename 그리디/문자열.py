class Solution:
    def solve(self, A:str, B:str) -> int:

        a_l = len(A)
        b_l = len(B)

        answer: int = 50
        for i in range(b_l-a_l+1):
            diff_cnt = 0
            for j in range(a_l):
                if A[j] != B[j+i]:
                    diff_cnt+=1
            answer = min(diff_cnt,answer)
        return answer



if __name__ == '__main__':
    A:str
    B:str
    A,B = input().split()

    s :Solution = Solution()
    print(s.solve(A,B))
