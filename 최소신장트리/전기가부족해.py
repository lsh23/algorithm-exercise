def find(x: int, parent: list[int]) -> int:
    if x == parent[x]:
        return x
    parent[x] = find(parent[x], parent)
    return parent[x]


def merge(x: int, y: int, parent: list[int], installed: list[int]):
    x: int = find(x, parent)
    y: int = find(y, parent)
    if x in installed and y in installed:
        return
    elif x not in installed and y not in installed:
        parent[y] = x
    else:
        if x in installed:
            parent[y] = x
        if y in installed:
            parent[x] = y


def is_uinon(x: int, y: int, parent: list[int]) -> bool:
    x: int = find(x, parent)
    y: int = find(y, parent)
    return x == y


class Solution:
    @staticmethod
    def solve(n: int, m: int, k: int, installed: list[int], edges: list[tuple[int, int, int]]) -> int:
        edges.sort()
        cnt: int = 0
        parent: list[int] = [i for i in range(n + 1)]
        mst_cost: int = 0
        for edge in edges:
            if cnt == n - 1:
                break
            w, u, v = edge
            if is_uinon(u, v, parent):
                continue
            if find(u, parent) in installed and find(v, parent) in installed:
                continue
            merge(u, v, parent)
            mst_cost += w

        return mst_cost


if __name__ == "__main__":
    N: int
    M: int
    K: int
    installed: list[int]

    N, M, K = map(int, input().split())
    installed = [int(x) for x in input().split()]

    edges: list[tuple[int, int, int]] = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    print(Solution.solve(N, M, K, installed, edges))
