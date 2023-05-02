import heapq

def prim(v: int, e: int, graph: list[list[tuple[int, int]]]) -> int:
    # 임의의 정점 선택
    # 간선 후보를 우선순위 큐에 넣는다.
    # 우선 순위큐에서 간선의 가중치가 가장 낮은 간선을 꺼내서 정점을 추가하고, 간선후보를 우선순위큐에 넣는다.
    # 모든 정점이 선택될때 까지

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


def find(x: int, parent: list[int]) -> int:
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x], parent)
        return parent[x]


def merge(x: int, y: int, parent: list[int]) -> None:
    x = find(x, parent)
    y = find(y, parent)
    if x == y:
        return
    parent[y] = x


def is_union(x: int, y: int, parent: list[int]) -> bool:
    return find(x, parent) == find(y, parent)


def kruskal(v: int, graph: list[list[tuple[int, int]]]) -> int:
    # 간선 정렬
    # 가장 작은 가중치 간선을 고르고 포함될 정점들에 대해 사이클 검사 ( 유니온 파인드로 )
    # 모든 정점이 선택될떄 까지
    ans: int = 0
    cnt: int = 0
    edges: list[tuple[int, int, int]] = []
    for i in range(len(graph)):
        for x in graph[i]:
            edges.append((x[1],i,x[0]))
    edges.sort()
    parent: list[int] = [i for i in range(v+1)]

    for edge in edges:
        if cnt == v-1:
            break
        weight, start, end = edge
        if is_union(start, end,parent):
            continue
        merge(start, end, parent)
        ans += weight
        cnt += 1

    return ans

class Solution:
    @staticmethod
    def solve(v: int, e: int, graph: list[list[tuple[int, int]]]) -> int:
        # return prim(v, e, graph)
        return kruskal(v, graph)


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
