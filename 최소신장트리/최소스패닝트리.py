import heapq


# 임의의 정점 선택
# 간선 후보를 우선순위 큐에 넣는다.
# 우선 순위큐에서 간선의 가중치가 가장 낮은 간선을 꺼내서 정점을 추가하고, 간선후보를 우선순위큐에 넣는다.
# 모든 정점이 선택될때 까지
def prim(v: int, e: int, graph: list[list[tuple[int, int]]]) -> int:
    checked: list[int] = [0] * v
    checked[0] = 1
    total_weight: int = 0

    q: list[tuple[int, int, int]] = []

    for edge in graph[0]:
        end, weight = edge
        heapq.heappush(q, (weight, 0, end))

    while not all(checked):
        weight, start, end = heapq.heappop(q)
        if checked[end] != 0:
            continue
        checked[end] = 1
        total_weight += weight
        for edge in graph[end]:
            next_end, weight = edge
            heapq.heappush(q, (weight, end, next_end))

    return total_weight


class Solution:
    @staticmethod
    def solve(v: int, e: int, graph: list[list[tuple[int, int]]]) -> int:
        return prim(v, e, graph)


if __name__ == "__main__":
    V: int
    E: int
    graph: list[list[tuple[int, int]]]
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        i, j, weight = map(int, input().split())
        graph[i - 1].append([j - 1, weight])
        graph[j - 1].append([i - 1, weight])
    print(Solution.solve(V, E, graph))
