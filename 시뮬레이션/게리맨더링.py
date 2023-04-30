from collections import deque


class Solution:
    @staticmethod
    def solve(N: int, popularity: list[int], graph: list[list[int]]) -> int:

        def is_valid_group(selected: list[int]) -> bool:
            if len(selected) == 1:
                return True

            checked: list[int] = [0] * N

            q: deque[int] = deque()
            q.append(selected[0])
            checked[selected[0]] = 1

            while q:
                v = q.popleft()
                for x in graph[v]:
                    if x not in selected:
                        continue
                    if checked[x] != 0:
                        continue
                    checked[x] = 1
                    q.append(x)

            for s in selected:
                if checked[s] == 0:
                    return False

            return True

        def combinations(l: int, k: int, n: int, selected: list[int]):
            nonlocal ans
            if l == n:

                others: list[int] = [i for i in range(N)]
                for s in selected:
                    others.remove(s)
                if is_valid_group(selected) is False or is_valid_group(others) is False:
                    return

                diff: int = abs(sum([popularity[x] for x in selected]) - sum([popularity[x] for x in others]))

                ans = min(diff, ans)
            else:
                for i in range(k, N):
                    selected[l] = i
                    combinations(l + 1, i + 1, n, selected)

        ans: int = 10000

        for i in range(1, (N // 2) + 1):
            combinations(0, 0, i, [0] * i)

        if ans == 10000:
            return -1

        return ans


if __name__ == "__main__":
    N: int
    popularity: list[int]
    graph: list[list[int]]

    N = int(input())
    popularity = [int(x) for x in input().split()]
    graph = [[] * N for _ in range(N)]
    for i in range(N):
        adj_info: list[int] = [int(x) for x in input().split()]
        for adj in adj_info[1:]:
            graph[i].append(adj - 1)

    print(Solution.solve(N, popularity, graph))
