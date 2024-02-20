from typing import List


class Solution:
    def longestCommonPrefix(
        self,
        arr1: List[int],
        arr2: List[int],
    ) -> int:
        ans = 0

        arr1Prefixes = set()

        for num in arr1:
            prefix = num
            while prefix != 0:
                arr1Prefixes.add(prefix)
                prefix //= 10

        for num in arr2:
            prefix = num
            while prefix != 0:
                if prefix in arr1Prefixes:
                    ans = max(ans, len(str(prefix)))
                prefix //= 10

        return ans
