from collections import deque


class Solution:
    @staticmethod
    def solve(puyo: list[list[str]]) -> int:

        ans: int = 0
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        while True:
            # 연쇄작용 및 연쇄 여부 체크
            chain: bool = False
            for i in range(12):
                for j in range(6):
                    if puyo[i][j] != '.':
                        cnt: int = 1
                        visited: list[list[int]] = [[0] * 6 for _ in range(12)]
                        visited[i][j] = 1

                        q: deque[tuple[int, int]] = deque()
                        q.append((i, j))

                        while q:
                            y, x = q.popleft()
                            for k in range(4):
                                next_y = y + dy[k]
                                next_x = x + dx[k]
                                if next_y < 0 or next_y >= 12 or next_x < 0 or next_x >= 6:
                                    continue
                                if visited[next_y][next_x] != 0:
                                    continue
                                if puyo[next_y][next_x] != puyo[y][x]:
                                    continue
                                visited[next_y][next_x] = 1
                                q.append((next_y, next_x))
                                cnt += 1

                        if cnt >= 4:
                            chain = True
                            for m in range(12):
                                for n in range(6):
                                    if visited[m][n] == 1:
                                        puyo[m][n] = "."

            # print("----1")
            # for p in puyo:
            #     print(p)

            # 중력 작용
            for i in range(6):
                tmp = []
                for j in range(12):
                    if puyo[j][i] != '.':
                        tmp.append(puyo[j][i])

                tmp = ["."]*(12-len(tmp)) + tmp

                for j in range(12):
                    puyo[j][i] = tmp[j]

            # print("----2")
            # for p in puyo:
            #     print(p)

            # 연쇄 일어났으면 다시 1 부터, 안일어났으면 중단
            if chain is False:
                break

            ans += 1

        return ans


if __name__ == "__main__":
    puyo: list[list[str]]
    puyo = [[x for x in input()] for _ in range(12)]
    assert len(puyo) == 12 and len(puyo[0]) == 6
    print(Solution.solve(puyo))
