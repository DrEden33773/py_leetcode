from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def dfsTwice(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        sumList = []

        def firstDfs(root: Optional[TreeNode], depth: int = 0):
            if not root:
                return
            if len(sumList) <= depth:
                sumList.append(0)
            sumList[depth] += root.val
            firstDfs(root.left, depth + 1)
            firstDfs(root.right, depth + 1)

        def secondDfs(root: Optional[TreeNode], depth: int = 0):
            if not root:
                return
            lv, rv = (root.left.val if root.left else 0), (
                root.right.val if root.right else 0
            )
            shouldSub = lv + rv
            nextDepth = depth + 1
            if root.left:
                root.left.val = sumList[nextDepth] - shouldSub
                secondDfs(root.left, nextDepth)
            if root.right:
                root.right.val = sumList[nextDepth] - shouldSub
                secondDfs(root.right, nextDepth)

        firstDfs(root)
        root.val = 0
        secondDfs(root)
        return root

    def bfsTwice(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.val = 0
        queue = [root]

        while queue:
            newQueue = []
            currSum = 0
            # first bfs: calc sum of next depth
            for node in queue:
                if node.left:
                    newQueue.append(node.left)
                    currSum += node.left.val
                if node.right:
                    newQueue.append(node.right)
                    currSum += node.right.val
            # second bfs: assign `next depth sum - children sum` to children
            for node in queue:
                toSub = (node.left.val if node.left else 0) + (
                    node.right.val if node.right else 0
                )
                if node.left:
                    node.left.val = currSum - toSub
                if node.right:
                    node.right.val = currSum - toSub
            queue = newQueue

        return root

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.bfsTwice(root)
