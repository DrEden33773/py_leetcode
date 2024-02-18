from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        last_sum = nums[0] + nums[1]
        opt = 1
        nums = nums[2:]

        while len(nums) >= 2 and nums[0] + nums[1] == last_sum:
            nums = nums[2:]
            opt += 1

        return opt
