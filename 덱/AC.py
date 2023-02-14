from collections import deque


class Solution:
    def solve(self, n:int, func:str, arr:list[str]) -> str:
        dq: deque[str] = deque(arr)

        reverse: bool = False

        for c in func:

            if c == "R":
                reverse = not reverse
                continue

            if not dq:
                return "error"

            if reverse:
                dq.pop()
            else:
                dq.popleft()

        if reverse:
            dq.reverse()

        return "["+",".join(dq)+"]"


if __name__ == "__main__":
    T: int = int(input())
    for _ in range(T):
        func: str = input()
        N: int = int(input())
        arr = input()[1:-1].split(",")
        if len(arr) == 1 and arr[0] == '':
            arr = []
        s = Solution()
        print(s.solve(N, func, arr))
