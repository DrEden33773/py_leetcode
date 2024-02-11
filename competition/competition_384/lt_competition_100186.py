from operator import eq, gt, lt


class Solution:
    def matches(self, subArray: list[int], pattern: list[int]) -> bool:
        if not pattern:
            return True
        assert len(subArray) - 1 == len(pattern)
        for k, operand in enumerate(pattern):
            match operand:
                case 1:
                    opt = gt
                case 0:
                    opt = eq
                case -1:
                    opt = lt
            if not opt(subArray[k + 1], subArray[k]):
                return False
        return True

    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        ans = 0
        n, m = len(nums), len(pattern)
        for i in range(n - m):
            subArray = nums[i : i + m + 1]
            ans += int(self.matches(subArray, pattern))
        return ans
