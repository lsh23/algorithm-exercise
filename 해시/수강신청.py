import sys
class Solution:
    def solve(self, K:int, L:int ) -> None:
        d = dict()
        q = []
        for _ in range(L):
            student: str = input().strip()
            if student in d:
                d[student] += 1
            else:
                d[student] = 1
            q.append(student)

        cnt: int = 0
        for s in q:
            d[s] -= 1
            if d[s] == 0:
                print(s)
                cnt += 1
            if cnt == K:
                break

if __name__ == '__main__':
    input = sys.stdin.readline
    K: int
    L: int
    K,L = map(int, input().split())
    s :Solution = Solution()
    s.solve(K, L)
