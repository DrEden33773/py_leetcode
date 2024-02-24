from bisect import bisect_left
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def fill_array(self, node: Optional[TreeNode], arr: List[int]):
        if node:
            self.fill_array(node.left, arr)
            arr.append(node.val)
            self.fill_array(node.right, arr)

    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        if not root:
            return []

        arr = []
        self.fill_array(root, arr)

        res = []
        for val in queries:
            max_val, min_val = -1, -1
            i = bisect_left(arr, val)
            if i != len(arr):
                max_val = arr[i]
                if arr[i] == val:
                    min_val = arr[i]
                    res.append([min_val, max_val])
                    continue
            if i != 0:
                min_val = arr[i - 1]
            res.append([min_val, max_val])

        return res
