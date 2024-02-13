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
        xy: tuple[int, int],
        pred: Callable[[TreeNode, tuple[int, int]], None],
    ):
        if root:
            pred(root, xy)
            self.dfs(root.left, (xy[0] + 1, xy[1] - 1), pred)
            self.dfs(root.right, (xy[0] + 1, xy[1] + 1), pred)

    def sortInTheEnd(self, root: Optional[TreeNode]) -> list[list[int]]:
        nodes, ans = [], []

        def pred(node: TreeNode, xy: tuple[int, int]):
            nodes.append((xy[1], xy[0], node.val))

        self.dfs(root, (0, 0), pred)

        nodes.sort()

        lastCol: Optional[int] = None

        for col, _, val in nodes:
            if lastCol != col:
                lastCol = col
                ans.append([])
            ans[-1].append(val)

        return ans

    def preGroupedSort(self, root: Optional[TreeNode]) -> list[list[int]]:
        groups = dict[int, list[tuple[int, int]]]()

        def pred(node: TreeNode, xy: tuple[int, int]):
            if xy[1] in groups:
                groups[xy[1]].append((xy[0], node.val))
            else:
                groups[xy[1]] = [(xy[0], node.val)]

        self.dfs(root, (0, 0), pred)

        ans = []

        for _, items in sorted(groups.items()):
            items.sort()
            curr = list(map(lambda x: x[1], items))
            ans.append(curr)

        return ans

    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        return self.sortInTheEnd(root)
