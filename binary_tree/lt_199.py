from functools import cache
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @cache
    def dfs(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return [root.val] + right + left[len(right) :]

    @cache
    def bfs(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        queue, res = [root], []
        while queue:
            res.append(queue[-1].val)
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return res

    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        return self.bfs(root)
