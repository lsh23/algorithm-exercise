class Solution:
    def solve(self, N: int, C: int, ship_info: list[tuple[int, int, int]]) -> int:

        ans: int = 0

        capacity: list[int] = [C]*(N+1)
        ship_info.sort(key=lambda x: (x[1]))

        for info in ship_info:
            _from, _to, c = info

            ship_box_cnt: int = c

            for j in range(_from, _to):
                if capacity[j] == 0:
                    ship_box_cnt = 0
                    break
                ship_box_cnt = min(capacity[j], ship_box_cnt)

            # print("can ship_box_cnt", ship_box_cnt, end=" ")
            ans += ship_box_cnt

            for j in range(_from, _to):
                capacity[j] -= ship_box_cnt

            # print(capacity, ans)

        return ans


if __name__ == '__main__':
    N: int
    C: int
    M: int

    N, C = map(int, input().split())
    M = int(input())

    ship_info: list[tuple[int, int, int]] = []
    for _ in range(M):
        _from, _to, c = map(int, input().split())
        ship_info.append((_from, _to, c))

    s: Solution = Solution()
    print(s.solve(N, C, ship_info))
