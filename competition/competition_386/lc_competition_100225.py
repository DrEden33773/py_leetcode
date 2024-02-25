from typing import List


class Solution:
    def overlapOfTwo(
        self,
        lhsBottomLeft: List[int],
        lhsTopRight: List[int],
        rhsBottomLeft: List[int],
        rhsTopRight: List[int],
    ) -> int:
        # 1. No overlap
        if (
            lhsTopRight[0] <= rhsBottomLeft[0]
            or rhsTopRight[0] <= lhsBottomLeft[0]
            or lhsTopRight[1] <= rhsBottomLeft[1]
            or rhsTopRight[1] <= lhsBottomLeft[1]
        ):
            return 0
        # 2. Overlap
        x = min(lhsTopRight[0], rhsTopRight[0]) - max(
            lhsBottomLeft[0], rhsBottomLeft[0]
        )
        y = min(lhsTopRight[1], rhsTopRight[1]) - max(
            lhsBottomLeft[1], rhsBottomLeft[1]
        )
        s = min(x, y)
        return s * s

    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        maxSquare = 0
        n = len(bottomLeft)
        for i in range(n):
            for j in range(i + 1, n):
                maxSquare = max(
                    maxSquare,
                    self.overlapOfTwo(
                        bottomLeft[i], topRight[i], bottomLeft[j], topRight[j]
                    ),
                )
        return maxSquare
