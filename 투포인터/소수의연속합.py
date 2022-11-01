import sys
from typing import List
class Solution:
    def solve(self, N: int) -> int:
        numbers: List[int] = [0] * (N+1)
        for i in range(2,N+1):
            numbers[i]=i
        
        for i in range(2,N+1):
            if numbers[i]==0:
                continue
            for j in range(i+i,N+1,i):
                numbers[j]=0
        
        prime_numbers: List[int] = [ x for x in numbers if x!=0]
        p_l: int = len(prime_numbers)
        for i in range(1,p_l):
            prime_numbers[i]+=prime_numbers[i-1]

        prime_numbers.insert(0,0)
        # print(prime_numbers)

        l: int = 0
        r: int = 0

        answer: int = 0

        while l<=r and r<=p_l:
            sum :int = prime_numbers[r]-prime_numbers[l]
            if sum < N:
                r+=1
            elif sum > N:
                l+=1
            else:
                answer+=1
                l+=1

        return answer


if __name__ == '__main__':
    N: int = int(input())
    s :Solution = Solution()
    answer :int = s.solve(N)
    print(answer)