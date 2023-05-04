def find(x: int, parent: list[int]) -> int:
    if parent[x] == x:
        return x
    parent[x] = find(parent[x], parent)
    return parent[x]


def is_union(x: int, y: int, parent: list[int]) -> bool:
    return find(x, parent) == find(y, parent)


def union(x: int, y: int, parent: list[int]) -> None:
    x = find(x, parent)
    y = find(y, parent)
    if x != y:
        parent[y] = x


class Solution:
    @staticmethod
    def solve(n: int, m: int, edges: list[tuple[int, int, int]]) -> int:
        ans: int = 0

        max_weight: int = 0

        edges.sort()
        parent: list[int] = [i for i in range(n)]

        cnt: int = 0
        for edge in edges:
            if cnt == n:
                break
            weight, start, end = edge
            if is_union(start, end, parent):
                continue
            union(start, end, parent)
            ans += weight
            max_weight = max(weight, max_weight)
            cnt += 1

        return ans - max_weight


if __name__ == "__main__":
    N: int
    M: int
    N, M = map(int, input().split())
    edges: list[tuple[int, int, int]] = []
    for _ in range(M):
        start, end, weight = map(int, input().split())
        edges.append((weight, start - 1, end - 1))
    print(Solution.solve(N, M, edges))
