class Solution:
    def double_layer_of_loop(self, nums: list[int]) -> int:
        res, n = -1, len(nums)
        for begin in range(n):
            for end in range(begin + 1, n):
                length = end - begin + 1
                if nums[end] - nums[begin] == (length - 1) % 2:
                    res = max(res, length)
                else:
                    break
        return res

    def single_layer_of_loop(self, nums: list[int]) -> int:
        res, begin = -1, 0
        for end in range(1, len(nums)):
            length = end - begin + 1
            if nums[end] - nums[begin] == (length - 1) % 2:
                res = max(res, length)
            elif nums[end] - nums[end - 1] == 1:
                begin = end - 1
                res = max(res, 2)
            else:
                begin = end
        return res

    def alternatingSubarray(self, nums: list[int]) -> int:
        return self.single_layer_of_loop(nums)
