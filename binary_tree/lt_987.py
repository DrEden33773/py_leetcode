from typing import Callable, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def dfs(
        self,
        root: Optional[TreeNode],
        pos: tuple[int, int],
        pred: Callable[[TreeNode, tuple[int, int]], None],
    ):
        if root:
            pred(root, pos)
            row, col = pos
            self.dfs(root.left, (row + 1, col - 1), pred)
            self.dfs(root.right, (row + 1, col + 1), pred)

    def sortInTheEnd(self, root: Optional[TreeNode]) -> list[list[int]]:
        nodes, ans = [], []

        def pred(node: TreeNode, pos: tuple[int, int]):
            nodes.append((pos[1], pos[0], node.val))

        self.dfs(root, (0, 0), pred)

        lastCol: Optional[int] = None
        for col, _, val in sorted(nodes):
            if lastCol != col:
                lastCol = col
                ans.append([])
            ans[-1].append(val)

        return ans

    def preGroupedSort(self, root: Optional[TreeNode]) -> list[list[int]]:
        groups = dict[int, list[tuple[int, int]]]()

        def pred(node: TreeNode, pos: tuple[int, int]):
            if pos[1] in groups:
                groups[pos[1]].append((pos[0], node.val))
            else:
                groups[pos[1]] = [(pos[0], node.val)]

        self.dfs(root, (0, 0), pred)

        ans = []
        for _, items in sorted(groups.items()):
            ans.append([val for _, val in sorted(items)])

        return ans

    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        return self.sortInTheEnd(root)
