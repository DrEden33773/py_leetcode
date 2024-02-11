from functools import cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @cache
    def inorder(self, root: Optional[TreeNode]):
        if root:
            yield from self.inorder(root.left)
            yield root.val
            yield from self.inorder(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        ans = []
        for val in self.inorder(root):
            ans.append(val)
        return ans
