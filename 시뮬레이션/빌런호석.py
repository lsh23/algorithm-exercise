digital_n: list[list[int]] = [
    [1, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1],
]

dist: list[list[int]] = [[0] * 11 for _ in range(11)]

for i in range(10):
    for j in range(i + 1, 10):
        diff_cnt: int = 0
        for m in range(7):
            if digital_n[i][m] != digital_n[j][m]:
                diff_cnt += 1
        dist[i][j] = diff_cnt
        dist[j][i] = diff_cnt


class Solution:
    @staticmethod
    def solve(n: int, k: int, p: int, x: int) -> int:
        str_x: str = str(x).zfill(k)
        answer: int = 0

        def choose(l: int, selected: list[int], visited: list[int]):
            nonlocal answer
            if k == l:
                sum: int = 0
                for i in range(k):
                    sum += dist[int(str_x[i])][selected[i]]
                if sum <= p:
                    changed = "".join([str(x) for x in selected])
                    if int(changed) > n or int(changed) == 0:
                        return
                    if str_x == changed or len(changed) != k:
                        return
                    answer += 1

            else:
                for i in range(0, 11):
                    if visited[i] == 0:
                        selected[l] = i
                        choose(l + 1, selected, visited)

        choose(0, [0] * k, [0] * 11)

        return answer


if __name__ == "__main__":
    N: int
    K: int
    P: int
    X: int
    N, K, P, X = map(int, input().split())
    print(Solution.solve(N, K, P, X))
