class Tree:
    def __init__(self, x):
        self.value = x
        self.right = None
        self.left = None
        self.parent = None

    def get_subtree_size(self):
        if self.right == None and self.left == None:
            return 1

        right = 0
        left = 0

        if self.right:
            right = self.right.get_subtree_size()
        if self.left:
            left = self.left.get_subtree_size()

        return right + left + 1


T = int(input())
for test_case in range(1, T + 1):
    V, E, A, B = map(int, input().split())
    edges = [int(x) for x in input().split()]
    edges = [(edges[2 * i], edges[2 * i + 1]) for i in range(E)]
    vertex = [Tree(i) for i in range(V + 1)]
    for edge in edges:
        parent, child = edge
        p = vertex[parent]
        c = vertex[child]
        c.parent = p
        if p.left:
            p.right = c
        else:
            p.left = c

    visited = [0] * (V + 1)

    # A의 부모 방문
    parent = vertex[A].parent
    while parent:
        visited[parent.value] = 1
        parent = parent.parent

    parent = vertex[B].parent
    while True:
        if visited[parent.value] == 1:
            break
        parent = parent.parent

    answer = parent.get_subtree_size()
    print(f'#{test_case} {parent.value} {answer}')
