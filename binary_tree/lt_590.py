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
            if root.children:
                for child in root.children:
                    self.recurse(child)
            self.recursiveRes.append(root.val)

    def postorder(self, root: Optional[Node]) -> list[int]:
        self.recurse(root)
        return self.recursiveRes
