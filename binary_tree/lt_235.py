from functools import cache
from typing import Optional


class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @cache
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root or not p or not q:
            return None
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
