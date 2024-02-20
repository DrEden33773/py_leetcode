from typing import List


class Solution:
    def isPrefix(self, pat: str, raw: str) -> bool:
        if len(pat) > len(raw):
            return False
        for patC, rawC in zip(pat, raw):
            if patC != rawC:
                return False
        return True

    def isPrefixAndSuffix(self, pat: str, raw: str) -> bool:
        return self.isPrefix(pat, raw) and self.isPrefix(pat[::-1], raw[::-1])

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        if len(words) < 2:
            return 0
        n, cnt = len(words), 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    cnt += 1
        return cnt
