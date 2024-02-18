from functools import cache
from typing import List


class Solution:
    """
    Given an array of integers called nums, you can perform any of the following operation while nums contains at least 2 elements:

    - Choose the first two elements of nums and delete them.
    - Choose the last two elements of nums and delete them.
    - Choose the first and the last elements of nums and delete them.

    The score of the operation is the sum of the deleted elements.

    Your task is to find the maximum number of operations that can be performed, such that all operations have the same score.

    Return the maximum number of operations possible that satisfy the condition mentioned above.

    Example 1:

    ```
    Input: nums = [3,2,1,2,3,4]
    Output: 3
    Explanation: We perform the following operations:
    - Delete the first two elements, with score 3 + 2 = 5, nums = [1,2,3,4].
    - Delete the first and the last elements, with score 1 + 4 = 5, nums = [2,3].
    - Delete the first and the last elements, with score 2 + 3 = 5, nums = [].
    We are unable to perform any more operations as nums is empty.
    ```

    Example 2:

    ```
    Input: nums = [3,2,6,1,4]
    Output: 2
    Explanation: We perform the following operations:
    - Delete the first two elements, with score 3 + 2 = 5, nums = [6,1,4].
    - Delete the last two elements, with score 1 + 4 = 5, nums = [6].
    It can be proven that we can perform at most 2 operations.
    ```
    """

    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        n = len(nums)

        @cache
        def dfs(l: int, r: int, sum: int) -> int:
            if r - l < 2:
                return 0
            ans = 0
            if nums[l] + nums[l + 1] == sum:
                ans = 1 + dfs(l + 2, r, sum)
            if nums[l] + nums[r - 1] == sum:
                ans = max(ans, 1 + dfs(l + 1, r - 1, sum))
            if nums[r - 2] + nums[r - 1] == sum:
                ans = max(ans, 1 + dfs(l, r - 2, sum))
            return ans

        return 1 + max(
            dfs(0, n - 2, nums[-1] + nums[-2]),
            dfs(2, n, nums[0] + nums[1]),
            dfs(1, n - 1, nums[0] + nums[-1]),
        )
