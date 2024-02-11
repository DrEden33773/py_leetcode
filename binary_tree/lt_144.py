from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def recursivePreOrderGenerator(self, root: Optional[TreeNode]):
        if root:
            yield root.val
            yield from self.recursivePreOrderGenerator(root.left)
            yield from self.recursivePreOrderGenerator(root.right)

    def iterativePreOrderGenerator(self, root: Optional[TreeNode]):
        stack = []
        while root or stack:
            while root:
                yield root.val
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right if root else None

    def iterativePreOrder(self, root: Optional[TreeNode]):
        stack, ans = [], []
        while root or stack:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right if root else None
        return ans

    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # assert list(self.recursivePreOrder(root)) == list(self.iterativePreOrder(root))
        return self.iterativePreOrder(root)
