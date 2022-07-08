from typing import List
class Solution:
    def solve(self, N:int, M:int, arr:List[int], arr2:List[int]) -> None:
        for k in arr2:
            l: int = 0
            r: int = N - 1
            while l<=r:
                mid: int = (l+r)//2
                if arr[mid] > k:
                    r = mid - 1
                elif arr[mid] < k:
                    l = mid + 1
                else:
                    print(1)
                    break
            if l>r:
                print(0)


if __name__ == '__main__':
    N: int = int(input())
    arr: List[int] = [int(x) for x in input().split()]
    arr.sort()
    M: int = int(input())
    arr2: List[int] = [int(x) for x in input().split()]
    s :Solution = Solution()
    s.solve(N,M,arr,arr2)
