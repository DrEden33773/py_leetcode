from collections import Counter


class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        ans = total = 0
        cnt = Counter()

        # `build`
        for word in words:
            total += len(word)
            cnt += Counter(word)

        # `sub` the letter which appeared odd times
        total -= sum(c % 2 for c in cnt.values())

        # get the those letters which appeared less first
        words.sort(key=len)

        for word in words:
            total -= len(word) // 2 * 2
            if total < 0:
                break
            ans += 1

        return ans
