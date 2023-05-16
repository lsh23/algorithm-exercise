class Solution:
    @staticmethod
    def solve(n: int, d: int, k: int, c: int, sushi: list[int]) -> int:
        l: int = 0
        ans: int = 0
        while l != n:
            sushi_set: set = set()
            for i in [(l + x) % n for x in range(k)]:
                sushi_set.add(sushi[i])
            sushi_set.add(c)
            ans = max(len(sushi_set), ans)
            l += 1
        return ans


if __name__ == "__main__":
    N: int
    d: int
    k: int
    c: int
    sushi: list[int]
    N, d, k, c = map(int, input().split())
    sushi = [int(input()) for _ in range(N)]
    print(Solution.solve(N, d, k, c, sushi))
