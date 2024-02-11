class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        toModify = []
        maxDict = {i: -2 for i in range(len(matrix[0]))}
        res = matrix

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                now = matrix[x][y]
                if now == -1:
                    toModify.append((x, y))
                elif now > maxDict[y]:
                    maxDict[y] = now

        for x, y in toModify:
            res[x][y] = maxDict[y]

        return res
