def rotate(r: int, c: int, s: int, A: list[list[int]]) -> None:

    tmp_A: list[list[int]] = [[x for x in y] for y in A]

    for k in range(s):
        for i in range(2*s-2*k):
            A[r-s-1+k][c-s+k+i] = tmp_A[r-s-1+k][c-s+k+i-1]
            A[r+s-1-k][c-s-1+k+i] = tmp_A[r+s-1-k][c-s+k+i]
            A[r-s-1+k+i][c-s-1+k] = tmp_A[r-s+k+i][c-s-1+k]
            A[r-s+k+i][c+s-1-k] = tmp_A[r-s+k+i-1][c+s-1-k]

    # for i in range(r - s - 1, r + s):
    #     for j in range(c - s - 1, c + s):
    #         print(A[i][j], end=" ")
    #     print()


def get_value(A: list[list[int]]) -> int:
    return min([sum(row) for row in A])


class Solution:
    @staticmethod
    def solve(n: int, m: int, k: int, A: list[list[int]], rotates: list[list[int]]) -> int:
        ans: int = 1000000000
        # 회전 연산 순서 정하기
        order: list[int] = [0] * k
        visited: list[int] = [0] * k

        def permutations(l: int):
            nonlocal ans
            if l == K:
                # 회전 연산 진행 후 A의 값 구하고 최솟값 갱신 하기
                cloned_A: list[list] = [[x for x in y] for y in A]
                for i in order:
                    r, c, s = rotates[i]
                    rotate(r, c, s, cloned_A)
                value: int = get_value(cloned_A)
                ans = min(value, ans)

            else:
                for i in range(k):
                    if visited[i] != 0:
                        continue
                    visited[i] = 1
                    order[l] = i
                    permutations(l + 1)
                    visited[i] = 0

        # 회전 연산 진행 후 A의 값 구하고 최솟값 갱신 하기
        permutations(0)
        return ans


if __name__ == "__main__":
    N: int
    M: int
    K: int
    A: list[list[int]]
    rotates: list[list[int]]
    N, M, K = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    rotates = [[int(x) for x in input().split()] for _ in range(K)]
    print(Solution.solve(N, M, K, A, rotates))
