from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        layer_sum = defaultdict[int, int](int)

        def dfs(node: Optional[TreeNode], layer: int = 0):
            if node:
                layer_sum[layer] += node.val
                dfs(node.left, layer + 1)
                dfs(node.right, layer + 1)

        dfs(root)
        sum_list = sorted(layer_sum.values(), reverse=True)
        i = k - 1

        return sum_list[i] if i < len(sum_list) else -1
