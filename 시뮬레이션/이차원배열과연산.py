class Solution:
    @staticmethod
    def solve(r: int, c: int, k: int, A: list[int]) -> int:
        # 3*3 배열 A에 1초 마다 R or C 연산을 진행하는데
        # 연산 진행후 A[r][c]의 값이 k인 최초 시간 출력
        ans: int = 0
        row_cnt: int = 3
        col_cnt: int = 3
        while A[r][c] != k and ans <= 100:
            # R 연산
            if row_cnt >= col_cnt:
                # 행에 대해서 빈도 수 구하기
                for i in range(1, row_cnt + 1):
                    cnt_bucket: list[int] = [0] * 101
                    for j in range(1, col_cnt + 1):
                        cnt_bucket[A[i][j]] += 1
                    size: int = 0
                    for cnt in range(1, 101):
                        for x in range(1, 101):
                            if cnt_bucket[x] == cnt:
                                A[i][size + 1] = x
                                A[i][size + 2] = cnt
                                size += 2
                            if size > 100:
                                break
                        if size > 100:
                            break
                    for x in range(size+1, 101):
                        A[i][x] = 0
                    if size > col_cnt:
                        col_cnt = size

            # C 연산
            else:
                for i in range(1, col_cnt + 1):
                    cnt_bucket: list[int] = [0] * 101
                    for j in range(1, row_cnt + 1):
                        cnt_bucket[A[j][i]] += 1

                    size: int = 0
                    for cnt in range(1, 101):
                        for x in range(1, 101):
                            if cnt_bucket[x] == cnt:
                                A[size + 1][i] = x
                                A[size + 2][i] = cnt
                                size += 2
                            if size > 100:
                                break
                        if size > 100:
                            break
                    for x in range(size + 1, 101):
                        A[x][i] = 0
                    if size > row_cnt:
                        row_cnt = size
            ans += 1

        if ans > 100:
            return -1
        return ans


if __name__ == "__main__":
    r: int
    c: int
    k: int
    A: list[list[int]] = [[0] * 101 for _ in range(101)]
    r, c, k = map(int, input().split())
    for i in range(1, 4):
        A[i][1], A[i][2], A[i][3] = map(int, input().split())
    print(Solution.solve(r, c, k, A))
