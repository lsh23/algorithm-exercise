import sys
from typing import List, Tuple
class Solution:
    def solve(self, n: int, numbers: List[int]) -> int:

        answer: int = 0

        zero_cnt = numbers.count(0)
        one_cnt = numbers.count(1)

        negative_numbers = [ x for x in numbers if x < 0]
        positive_numbers = [ x for x in numbers if x > 1]

        negative_numbers.sort()
        positive_numbers.sort(reverse=True)

        len_positive_numbers = len(positive_numbers)
        if  len_positive_numbers % 2 != 0:
            for i in range(0,len_positive_numbers-2,2):
                answer += (positive_numbers[i]*positive_numbers[i+1])
            answer += positive_numbers[-1]
        else:
            for i in range(0,len_positive_numbers-1,2):
                answer += (positive_numbers[i]*positive_numbers[i+1])

        len_negative_numbers = len(negative_numbers)
        if len_negative_numbers % 2 != 0:
            for i in range(0, len_negative_numbers - 2, 2):
                answer += (negative_numbers[i] * negative_numbers[i + 1])
            if (len_negative_numbers == 1 and zero_cnt == 0) or zero_cnt == 0:
                answer += negative_numbers[-1]
        else:
            for i in range(0, len_negative_numbers - 1, 2):
                answer += (negative_numbers[i] * negative_numbers[i + 1])

        answer += one_cnt

        return answer

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    numbers = [ int(input()) for _ in range(N)]
    s :Solution = Solution()
    answer :int = s.solve(N, numbers)
    print(answer)

