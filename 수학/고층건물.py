class Solution:
    @staticmethod
    def solve(n: int, buildings: list[int]) -> int:

        answer: int = 0

        for i in range(n):
            x1 = i
            y1 = buildings[x1]

            # 왼쪽 0~i
            # 가장 가까운 쪽 부터 기울기의 최소값 갱신 횟수
            min_gradient: int = 1_000_000_001
            left_cnt: int = 0
            for x in range(x1 - 1, -1, -1):
                y = buildings[x]

                gradient = (y - y1) / (x - x1)
                if min_gradient > gradient:
                    left_cnt += 1
                    min_gradient = gradient

            # 오른쪽 i,n-1
            # 가장 가까운 쪽 부터 기울기의 최댓값 갱신 횟수
            max_gradient: int = -1_000_000_001
            right_cnt: int = 0
            for x in range(i + 1, n):
                y = buildings[x]

                gradient = (y - y1) / (x - x1)
                if max_gradient < gradient:
                    right_cnt += 1
                    max_gradient = gradient

            answer = max(left_cnt + right_cnt, answer)

        return answer


if __name__ == "__main__":
    N: int
    buildings: list[int]
    N = int(input())
    buildings = [int(x) for x in input().split()]
    print(Solution.solve(N, buildings))
