class Solution:
    @staticmethod
    def solve(n: int, l: int, map_info: list[list[int]]) -> int:
        # 2N개의 길에 대해서
        # 경사로를 놓았을 때 지나 갈 수 있는지 확인

        ans: int = 2 * n

        # n개의 행에 대해 체크
        for i in range(n):
            # 길이가 바뀌는 지점을 찾는다
            # 낮은쪽의 길이가 L보다 크거나 같으면 된다
            cur = map_info[i][0]
            cur_cnt = 1
            j = 1
            while j < n:
                h_diff = abs(map_info[i][j] - cur)
                if h_diff > 1:  # 높이가 1보다 크면 나면 절때 지나갈 수 없음
                    ans -= 1
                    break
                elif h_diff == 0:
                    cur_cnt += 1
                else:
                    if cur > map_info[i][j]:
                        lower_cnt = 1
                        lower = map_info[i][j]
                        while j + 1 < n and lower == map_info[i][j + 1]:
                            lower_cnt += 1
                            j += 1
                        if lower_cnt < l:
                            ans -= 1
                            break
                        cur = lower
                        cur_cnt = lower_cnt - l
                    else:
                        if cur_cnt < l:  # 높이가 낮은쪽 길의 길이가 경사로 보다 작으면 경사로를 놓을수가 없음
                            ans -= 1
                            break
                        cur = map_info[i][j]
                        cur_cnt = 1
                j += 1

        # n개의 열에 대해 체크
        for i in range(n):
            # 길이가 바뀌는 지점을 찾는다
            # 낮은쪽의 길이가 L보다 크거나 같으면 된다
            cur = map_info[0][i]
            cur_cnt = 1
            j = 1
            while j < n:
                h_diff = abs(map_info[j][i] - cur)
                if h_diff > 1:  # 높이가 1보다 크면 나면 절때 지나갈 수 없음
                    ans -= 1
                    break
                elif h_diff == 0:
                    cur_cnt += 1
                else:
                    if cur > map_info[j][i]:
                        lower_cnt = 1
                        lower = map_info[j][i]
                        while j + 1 < n and lower == map_info[j + 1][i]:
                            lower_cnt += 1
                            j += 1
                        if lower_cnt < l:
                            ans -= 1
                            break
                        cur = lower
                        cur_cnt = lower_cnt - l
                    else:
                        if cur_cnt < l:  # 높이가 낮은쪽 길의 길이가 경사로 보다 작으면 경사로를 놓을수가 없음
                            ans -= 1
                            break
                        cur = map_info[j][i]
                        cur_cnt = 1
                j += 1
        return ans


if __name__ == "__main__":
    N: int
    L: int
    map_info: list[list[int]]
    N, L = map(int, input().split())
    map_info = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, L, map_info))
