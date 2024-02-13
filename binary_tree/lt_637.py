from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        if not root:
            return []

        ans, queue = [], [root]

        while queue:
            sum, cnt = 0, 0
            nextQueue = []
            for node in queue:
                sum += node.val
                cnt += 1
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            queue = nextQueue
            ans.append(sum / cnt)

        return ans
