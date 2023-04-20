class Solution:
    @staticmethod
    def solve(n: int, blocks: list[list[int]]) -> None:

        def find_col(t, x, y):
            if t == 1:
                c = 1
                for i in range(2, 6):
                    if blue[x][i] != 0:
                        break
                    c = i
            if t == 2:
                c = 1
                for i in range(2, 5):
                    if blue[x][i] != 0 or blue[x][i + 1] != 0:
                        break
                    c = i

                if c == 1 and blue[x][2] != 0:
                    c = 0

            if t == 3:
                c = 1
                for i in range(2, 6):
                    if blue[x][i] != 0 or blue[x + 1][i] != 0:
                        break
                    c = i
            return c

        def find_row(t, x, y):
            if t == 1:
                r = 1
                for i in range(2, 6):
                    if green[i][y] != 0:
                        break
                    r = i
            if t == 2:
                r = 1
                for i in range(2, 6):
                    if green[i][y] != 0 or green[i][y + 1] != 0:
                        break
                    r = i

            if t == 3:
                r = 1
                for i in range(2, 5):
                    if green[i][y] != 0 or green[i + 1][y] != 0:
                        break
                    r = i
                if r == 1 and green[2][y] != 0:
                    r = 0
            return r

        def put_t_to_blue(t, x, y, c):
            if t == 1:
                blue[x][c] = 1
            if t == 2:
                blue[x][c] = 1
                blue[x][c + 1] = 1
            if t == 3:
                blue[x][c] = 1
                blue[x + 1][c] = 1

        def put_t_to_gleen(t, x, y, r):
            if t == 1:
                green[r][y] = 1
            if t == 2:
                green[r][y] = 1
                green[r][y + 1] = 1
            if t == 3:
                green[r][y] = 1
                green[r + 1][y] = 1

        score: int = 0

        # blue board
        blue: list[list[int]] = [[0] * 6 for _ in range(4)]

        # green board
        green: list[list[int]] = [[0] * 4 for _ in range(6)]

        for block in blocks:
            t, x, y = block
            c = find_col(t, x, y)
            put_t_to_blue(t, x, y, c)
            # blue는 마지막 열 부터 거꾸로 올라오면서 놓을 열을 찾는다.
            # 0또는 1열에 놓게되면 오른쪽으로 시프트

            # 열에 모든칸이 꽉차면 해당 열을 지우고 지워진 열의 수만큼 오른쪽으로 시프트
            while True:
                full: bool = False
                for i in range(5, 1, -1):
                    if all([blue[j][i] for j in range(4)]):
                        new_blue = [[x for x in y] for y in blue]
                        for x in range(4):
                            for j in range(1, i + 1):
                                new_blue[x][j] = blue[x][j - 1]
                        new_blue[0][0] = 0
                        new_blue[1][0] = 0
                        new_blue[2][0] = 0
                        new_blue[3][0] = 0
                        blue = new_blue
                        full = True
                        score += 1
                        c += 1
                        break
                if full is False:
                    break

            if c == 0 or c == 1:
                # blue_right_shift()
                new_blue = [[0] * 6 for _ in range(4)]
                for i in range(4):
                    for j in range(2, 6):
                        new_blue[i][j] = blue[i][(j - (2 - c))]
                blue = new_blue

            # print("b")
            # for b in blue:
            #     print(b)

            # green은 마지막 행 부터 거꾸로 올라오면서 놓을 행을 찾는다.
            r = find_row(t, x, y)
            put_t_to_gleen(t, x, y, r)
            # 행에 모든칸이 꽉차면 해당 행을 지우고 지워진 행의 수만큼 아래로 시프트
            while True:
                full: bool = False
                for i in range(5, 1, -1):
                    if all([green[i][j] for j in range(4)]):
                        new_green = [[x for x in y] for y in green]
                        for j in range(1, i + 1):
                            for x in range(4):
                                new_green[j][x] = green[j - 1][x]
                        new_green[0] = [0] * 4
                        green = new_green
                        full = True
                        score += 1
                        r += 1
                        break
                if full is False:
                    break

            # 0또는 1행에 놓게되면 아래쪽으로 시프트
            if r == 0 or r == 1:
                # green_down_shift(c)
                new_green = [[0] * 4 for _ in range(6)]
                for i in range(2, 6):
                    for j in range(4):
                        new_green[i][j] = green[i - (2 - r)][j]
                green = new_green

            # print("g")
            # for g in green:
            #     print(g)

        cnt: int = 0
        for i in range(4):
            for j in range(6):
                if blue[i][j] == 1:
                    cnt += 1
                if green[j][i] == 1:
                    cnt += 1

        print(score)
        print(cnt)


if __name__ == "__main__":
    N: int
    blocks: list[list[int]]
    N = int(input())
    blocks = [[int(x) for x in input().split()] for _ in range(N)]
    Solution.solve(N, blocks)
