def rotate(sticker: list[list[int]], cnt: int) -> list[list[int]]:
    s_r = len(sticker)
    s_c = len(sticker[0])

    if cnt == 0:
        return sticker

    if cnt == 1:
        rotated_sticker = [[0] * s_r for _ in range(s_c)]
        for i in range(s_c):
            for j in range(s_r):
                rotated_sticker[i][j] = sticker[j][i]
        rotated_sticker = [r[::-1] for r in rotated_sticker]
        return rotated_sticker

    if cnt == 2:
        rotated_sticker = [r[::-1] for r in sticker[::-1]]
        return rotated_sticker

    if cnt == 3:
        rotated_sticker = [[0] * s_r for _ in range(s_c)]
        for i in range(s_c):
            for j in range(s_r):
                rotated_sticker[i][j] = sticker[j][i]
        rotated_sticker = [r[::] for r in rotated_sticker[::-1]]

        return rotated_sticker


def find_location(sticker: list[list[int]], notebook: list[list[int]]) -> tuple:
    n_r = len(notebook)
    n_c = len((notebook[0]))
    s_r = len(sticker)
    s_c = len(sticker[0])

    for i in range(n_r - s_r + 1):
        for j in range(n_c - s_c + 1):
            can_paste: bool = True
            for k in range(s_r):
                if can_paste:
                    for l in range(s_c):
                        if sticker[k][l] == 1 and notebook[i + k][j + l] == 1:
                            can_paste = False
                            break
            if can_paste:
                return (i, j)

    return (-1, -1)


def paste(loc: tuple[int, int], rotated_sticker: list[list[int]], notebook: list[list[int]]):
    y, x = loc
    s_r = len(rotated_sticker)
    s_c = len(rotated_sticker[0])

    for i in range(s_r):
        for j in range(s_c):
            if rotated_sticker[i][j]:
                notebook[y + i][x + j] = rotated_sticker[i][j]


class Solution:
    @staticmethod
    def solve(n: int, m: int, k: int, stickers: list[list[list[int]]]) -> int:
        ans: int = 0
        notebook: list[list[int]] = [[0] * m for _ in range(n)]

        # 모든 스티커에 대해서
        # 0, 90, 180, 270 회전 후 붙일 위치 찾기
        # 찾았으면 붙이고, 없으면 버리기
        for s in stickers:
            # print("s")
            # for z in s:
            #     print(z)
            for i in range(4):
                rotated_sticker = rotate(s, i)
                # print("r_ s", i)
                # for z in rotated_sticker:
                #     print(z)
                y, x = find_location(rotated_sticker, notebook)
                if y == -1 and x == -1:
                    continue
                paste((y, x), rotated_sticker, notebook)
                # for x in notebook:
                #     print(x)
                break

        # 스티커 붙은 칸의 수 세기
        for i in range(n):
            for j in range(m):
                if notebook[i][j] == 1:
                    ans += 1

        return ans


if __name__ == "__main__":
    N: int
    M: int
    K: int
    stickers: list[list[list[int]]] = []
    N, M, K = map(int, input().split())

    for _ in range(K):
        R: int
        C: int
        R, C = map(int, input().split())
        sticker: list[list[int]] = [[int(x) for x in input().split()] for _ in range(R)]
        assert len(sticker) == R and len(sticker[0]) == C
        stickers.append(sticker)

    print(Solution.solve(N, M, K, stickers))
