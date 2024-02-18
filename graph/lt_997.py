from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        table = {i + 1: [0, 0] for i in range(n)}

        for src, dst in trust:
            table[src][1] += 1
            table[dst][0] += 1

        for k, v in table.items():
            if v[0] == n - 1 and v[1] == 0:
                return k

        return -1
