from itertools import combinations


class Solution:
    @staticmethod
    def solve(n: int, s_ij: list[list[int]]):
        ans: int = 40001

        members = [i for i in range(n)]

        # N/2 명씩 팀나누기
        for start_team in combinations(members, N // 2):
            link_team = []
            for member in members:
                if member in start_team:
                    continue
                link_team.append(member)
            # 스타트팀, 링크팀 능력치 구하기
            start_stat = 0
            link_stat = 0
            for i in range(N // 2):
                for j in range(N // 2):
                    start_stat += s_ij[start_team[i]][start_team[j]]
                    link_stat += s_ij[link_team[i]][link_team[j]]
            diff = abs(start_stat - link_stat)
            # 팀 능력치 차 최솟값 갱신
            ans = min(diff, ans)

        return ans


if __name__ == "__main__":
    N: int
    S_ij: list[list[int]]
    N = int(input())
    S_ij = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, S_ij))
