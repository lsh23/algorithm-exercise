from functools import reduce


class Solution:
    def solve(self, map_cloth_type_cnt: dict[str, int]) -> int:
        return reduce(lambda result, cur: result*(cur+1), map_cloth_type_cnt.values(), 1)-1


if __name__ == "__main__":
    T: int
    T = int(input())
    for _ in range(T):
        N: int
        N = int(input())
        h: dict[str, int] = {}
        for _ in range(N):
            cloth_name: str
            cloth_type: str
            cloth_name, cloth_type = input().split(" ")

            if cloth_type in h:
                h[cloth_type] += 1
            else:
                h[cloth_type] = 1

        s: Solution = Solution()
        print(s.solve(h))
