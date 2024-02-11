from typing import Optional


class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if (not root) or (not p) or (not q):
            return None

        # bfs to get fatherDict
        fatherDict: dict[TreeNode, Optional[TreeNode]] = {root: None}
        queue = [root]
        while queue:
            currLayer = []
            for node in queue:
                if node.left:
                    fatherDict[node.left] = node
                    currLayer.append(node.left)
                if node.right:
                    fatherDict[node.right] = node
                    currLayer.append(node.right)
            queue = currLayer

        # jump back (do not try to jump back at the same time)
        # (use HashSet instead)
        visited = set[TreeNode]()
        # first, go with p
        while p:
            visited.add(p)
            p = fatherDict[p]
        # then, go with q
        while q:
            if q in visited:
                return q
            q = fatherDict[q]

        return None
