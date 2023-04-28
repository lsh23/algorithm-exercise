def check_finish(paper_info: list[list[int]]) -> bool:
    for i in range(10):
        for j in range(10):
            if paper_info[i][j] == 1:
                return False
    return True


def check_piece(y: int, x: int, paper_info: list[list[int]], k: int, piece_cnt: list[int]) -> bool:
    if piece_cnt[k] >= 5:
        return False

    if y + k >= 10 or x + k >= 10:
        return False

    for i in range(y, y + k + 1):
        for j in range(x, x + k + 1):
            if paper_info[i][j] != 1:
                return False

    return True


def fill(y: int, x: int, paper_info: list[list[int]], k: int, piece_cnt: list[int]):
    piece_cnt[k] += 1
    for i in range(y, y + k + 1):
        for j in range(x, x + k + 1):
            paper_info[i][j] = -(k + 1)


def rollback(y: int, x: int, paper_info: list[list[int]], k: int, piece_cnt: list[int]):
    piece_cnt[k] -= 1
    for i in range(y, y + k + 1):
        for j in range(x, x + k + 1):
            paper_info[i][j] = 1


class Solution:
    @staticmethod
    def solve(paper_info: list[list[int]]) -> int:
        ans: int = 26

        # 붙일때는 경계 밖으로 나가서는 안되고, 서로 겹처도 안되고, 칸의 경계와 일치하게 붙여야 한다.
        def dfs(y: int, x: int, piece_cnt: list[int], paper_info: list[list]):
            nonlocal ans

            if check_finish(paper_info) == True:  # 최솟값 갱신 및 종료 조건
                ans = min(sum(piece_cnt), ans)
                return

            if sum(piece_cnt) > ans:  # 최솟값 보다 많이 색종이를 사용한 경우
                return

            if y == 10:  # 범위를 벗어난 경우
                return

            if paper_info[y][x] != 1:
                if x + 1 == 10:
                    dfs(y + 1, 0, piece_cnt, paper_info)
                else:
                    dfs(y, x + 1, piece_cnt, paper_info)
            else:
                for k in range(4, -1, -1):
                    if check_piece(y, x, paper_info, k, piece_cnt):
                        fill(y, x, paper_info, k, piece_cnt)
                        if x + 1 == 10:
                            dfs(y + 1, 0, piece_cnt, paper_info)
                        else:
                            dfs(y, x + 1, piece_cnt, paper_info)
                        rollback(y, x, paper_info, k, piece_cnt)

        dfs(0, 0, [0, 0, 0, 0, 0], paper_info)

        if ans == 26:
            return -1
        return ans


if __name__ == "__main__":
    paper_info: list[list[int]] = [[int(x) for x in input().split()] for _ in range(10)]
    print(Solution.solve(paper_info))
