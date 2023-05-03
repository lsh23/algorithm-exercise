dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


class Solution:
    @staticmethod
    def solve(n: int, students: list[list[int]]) -> int:
        ans: int = 0

        seats: list[list[int]] = [[0] * n for _ in range(n)]
        student_to_like_map: dict[int, list[int]] = {}
        for student in students:
            number, *like = student
            student_to_like_map[number] = like
            y: int = 21
            x: int = 21
            max_like_adj_cnt: int = 0
            max_empty_adj_cnt: int = 0
            for i in range(n):
                for j in range(n):
                    if seats[i][j] != 0:
                        continue
                    like_adj_cnt: int = 0
                    empty_adj_cnt: int = 0
                    for k in range(4):
                        ny = i + dy[k]
                        nx = j + dx[k]
                        if ny < 0 or ny >= n or nx < 0 or nx >= n:
                            continue
                        if seats[ny][nx] == 0:
                            empty_adj_cnt += 1
                        if seats[ny][nx] in like:
                            like_adj_cnt += 1
                    if max_like_adj_cnt < like_adj_cnt:
                        y = i
                        x = j
                        max_like_adj_cnt = like_adj_cnt
                        max_empty_adj_cnt = empty_adj_cnt
                        continue
                    if max_like_adj_cnt == like_adj_cnt:
                        if max_empty_adj_cnt < empty_adj_cnt:
                            y = i
                            x = j
                            max_empty_adj_cnt = empty_adj_cnt
                            continue
                        if max_empty_adj_cnt == empty_adj_cnt:
                            if i < y:
                                y = i
                                x = j
                                continue
                            if i == y:
                                if j < x:
                                    y = i
                                    x = j

            seats[y][x] = number

        for i in range(n):
            for j in range(n):
                number = seats[i][j]
                like_adj_cnt: int = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue
                    if seats[ny][nx] in student_to_like_map[number]:
                        like_adj_cnt += 1
                if like_adj_cnt == 0:
                    continue
                ans += 10 ** (like_adj_cnt - 1)

        return ans


if __name__ == "__main__":
    N: int
    students: list[list[int]]
    N = int(input())
    students = [[int(x) for x in input().split()] for _ in range(N ** 2)]
    print(Solution.solve(N, students))
