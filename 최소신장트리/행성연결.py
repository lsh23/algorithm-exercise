def merge(x: int, y: int, parent: list[int]):
    x = find(x, parent)
    y = find(y, parent)
    if x != y:
        parent[y] = x


def find(x: int, parent: list[int]) -> int:
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x], parent)
        return parent[x]


def is_union(x: int, y: int, parent: list[int]) -> bool:
    x = find(x, parent)
    y = find(y, parent)
    return x == y


class Solution:
    @staticmethod
    def solve(n: int, graph: list[list[int]]) -> int:

        edges: list[tuple[int, int, int]] = []

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((graph[i][j], i, j))

        edges.sort()

        parent: list[int] = [i for i in range(n)]

        ans: int = 0
        cnt: int = 1
        for edge in edges:
            if cnt == n:
                break
            weight, start, end = edge
            if is_union(start, end, parent):
                continue
            merge(start, end, parent)
            ans += weight
            cnt += 1

        return ans


if __name__ == "__main__":
    N: int
    graph: list[list[int]]
    N = int(input())
    graph = [[int(x) for x in input().split()] for _ in range(N)]
    print(Solution.solve(N, graph))
