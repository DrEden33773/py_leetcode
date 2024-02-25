from collections import Counter
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for freq in cnt.values():
            if freq > 2:
                return False
        return True
