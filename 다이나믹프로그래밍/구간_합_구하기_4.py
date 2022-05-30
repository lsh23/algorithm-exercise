from typing import List
import sys
class Solution:
    def DP(self, i:int, j:int, numbers:List[int]) -> int:
        return numbers[j]-numbers[i-1]

if __name__ == '__main__':
    import time

    start = time.time()  # 시작 시간 저장



    N,M = map(int,sys.stdin.readline().split())
    numbers = list(map(int,sys.stdin.readline().split()))
    numbers.insert(0,0)

    for i in range(1,N+1):
        numbers[i] = numbers[i] + numbers[i-1]

    # s = Solution()
    for _ in range(M):
        i,j = map(int,sys.stdin.readline().split())
        # print(s.DP(i,j,numbers))
        print(numbers[j] - numbers[i - 1])


    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간