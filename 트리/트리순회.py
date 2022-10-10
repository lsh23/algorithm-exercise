from typing import List

class Node:
    pass

class Node:
    value = ""
    left = None
    right = None

    def __init__(self,value:str):
        self.value = value

    def set_left(self, left_node: Node):
        self.left = left_node

    def set_right(self, right_node: Node):
        self.right = right_node

    def preorder(self):
        print(self, end="")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self, end="")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self, end="")

    def __str__(self):
        return self.value

class Solution:
    def solve(self, N:int, P:int, Q:int) -> int:

        cache = dict()
        cache[0] = 1
        def dp(k):
            if k==0:
                return 1
            else:
                if k in cache.keys():
                    return cache[k]
                else:
                    cache[k] = dp(k//P) + dp(k//Q)
                    return cache[k]
        return dp(N)

if __name__ == '__main__':
    N:int = int(input())
    node_dict: dict[str,Node] = {}
    root_node = Node('A')
    node_dict['A'] = root_node

    for _ in range(N):
        parent: str
        left: str
        right: str
        parent, left, right = input().split()
        parent_node = node_dict[parent]

        if left != '.':
            left_node = Node(left)
            node_dict[left] = left_node
            parent_node.set_left(left_node)

        if right != '.':
            right_node = Node(right)
            node_dict[right] = right_node
            parent_node.set_right(right_node)

    root_node.preorder()
    print()
    root_node.inorder()
    print()
    root_node.postorder()


