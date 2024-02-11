from typing import Optional


class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children: Optional[list[Node]] = children


class Solution:
    def levelOrder(self, root: Optional[Node]) -> list[list[int]]:
        if not root:
            return []

        queue, res = [root], []

        while queue:
            nextQueue, currLayer = [], []
            for node in queue:
                currLayer.append(node.val)
                if node.children:
                    nextQueue.extend(node.children)
            res.append(currLayer)
            queue = nextQueue

        return res
