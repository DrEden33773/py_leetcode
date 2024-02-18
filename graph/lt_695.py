from typing import List


class Solution:
    def __init__(self) -> None:
        self.maxArea = 0

    def bfs(self, x: int, y: int, grid: List[List[int]]) -> int:
        area, queue = 0, [(x, y)]
        grid[x][y] = 0

        while queue:
            nextQueue = []
            for cx, cy in queue:
                area += 1
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = cx + dx, cy + dy
                    if (
                        0 <= nx < len(grid)
                        and 0 <= ny < len(grid[0])
                        and grid[nx][ny] == 1
                    ):
                        nextQueue.append((nx, ny))
                        grid[nx][ny] = 0
            queue = nextQueue

        return area

    def dfs(self, x: int, y: int, grid: List[List[int]]) -> int:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
            grid[x][y] = 0
            return (
                1
                + self.dfs(x + 1, y, grid)
                + self.dfs(x - 1, y, grid)
                + self.dfs(x, y + 1, grid)
                + self.dfs(x, y - 1, grid)
            )
        return 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        X, Y = len(grid), len(grid[0])
        for x in range(X):
            for y in range(Y):
                if grid[x][y] == 1:
                    self.maxArea = max(self.maxArea, self.bfs(x, y, grid))
                    # self.maxArea = max(self.maxArea, self.dfs(x, y, grid))
        return self.maxArea
