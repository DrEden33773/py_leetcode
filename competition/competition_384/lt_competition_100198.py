from itertools import pairwise


class StringHash:
    def __init__(self, seq: str) -> None:
        n = len(seq)
        p = 1313131
        hash = [0] * (n + 10)
        prime = [1] * (n + 10)

        for i in range(n):
            prime[i + 1] = prime[i] * p
            hash[i + 1] = hash[i] * p + ord(seq[i])

        self.p = p
        self.hash = hash
        self.prime = prime

    def getSubStrHash(self, start: int, end: int) -> int:
        return self.hash[end] - self.hash[start] * self.prime[end - start]


class Solution:
    def stringHash(self, nums: list[int], pattern: list[int]) -> int:
        ans = 0

        for i in range(len(pattern)):
            pattern[i] += 1
        patternStr = "".join(map(str, pattern))
        transformed = list((y > x) - (y < x) + 1 for x, y in pairwise(nums))
        transformedStr = "".join(map(str, transformed))

        transformedStrHasher = StringHash(transformedStr)
        patternStrHash = StringHash(patternStr).getSubStrHash(0, len(patternStr))
        n, p = len(transformed), len(pattern)

        for i in range(n - p + 1):
            if transformedStrHasher.getSubStrHash(i, i + p) == patternStrHash:
                ans += 1

        return ans

    def kmp(self, nums: list[int], pattern: list[int]) -> int:
        m = len(pattern)
        pi = [0] * m
        cnt = 0
        for i in range(1, m):
            v = pattern[i]
            while cnt and pattern[cnt] != v:
                cnt = pi[cnt - 1]
            if pattern[cnt] == v:
                cnt += 1
            pi[i] = cnt

        ans = cnt = 0
        for x, y in pairwise(nums):
            v = (y > x) - (y < x)
            while cnt and pattern[cnt] != v:
                cnt = pi[cnt - 1]
            if pattern[cnt] == v:
                cnt += 1
            if cnt == m:
                ans += 1
                cnt = pi[cnt - 1]

        return ans

    def zAlgorithm(self, nums: list[int], pattern: list[int]) -> int:
        m = len(pattern)
        pattern.append(2)
        pattern.extend((y > x) - (y < x) for x, y in pairwise(nums))

        n = len(pattern)
        z = [0] * n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(z[i - l], r - i + 1)
            while i + z[i] < n and pattern[z[i]] == pattern[i + z[i]]:
                l, r = i, i + z[i]
                z[i] += 1

        return sum(lcp == m for lcp in z[m + 1 :])

    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        return self.kmp(nums, pattern)
