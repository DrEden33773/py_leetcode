from typing import Optional


class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children: Optional[list[Node]] = children


class Solution:
    def __init__(self) -> None:
        self.recursiveRes = []

    def recurse(self, root: Optional[Node]):
        if root:
            self.recursiveRes.append(root.val)
            if root.children:
                for child in root.children:
                    self.recurse(child)

    def iterative(self, root: Optional[Node]) -> list[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                for child in node.children[::-1]:
                    stack.append(child)
        return res

    def preorder(self, root: Optional[Node]) -> list[int]:
        return self.iterative(root)
