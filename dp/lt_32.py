class Solution:
    def greedy(self, s: str) -> int:
        """Iterate twice!"""

        left, right, maxLen = 0, 0, 0

        # iterate from left to right => discard abundant right
        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, 2 * right)
            elif right > left:
                left, right = 0, 0

        left, right = 0, 0

        # iterate from right to left => discard abundant left
        for c in s[::-1]:
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, 2 * left)
            elif left > right:
                left, right = 0, 0

        return maxLen

    def stack(self, s: str) -> int:
        """
        stack[0] (bottom) => the last unmatched `)`'s index
        stack[1:] => unmatched `(`'s index
        """
        if len(s) <= 1:
            return 0

        # bottom of `stack` is the record of last unmatched `)`
        stack, ans = [-1], 0

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                stack.pop()
                if len(stack) == 0:
                    # stack has just popped an illegal `)`, not `(`
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans

    def longestValidParentheses(self, s: str) -> int:
        return self.greedy(s)
