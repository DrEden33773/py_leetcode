class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        max_i = n - 1
        i1 = i2 = -1
        for i in reversed(range(0, n)):
            if s[i] > s[max_i]:
                max_i = i
            elif s[i] < s[max_i]:
                i1, i2 = i, max_i
        if i1 < 0:
            return num
        s[i1], s[i2] = s[i2], s[i1]
        return int("".join(s))
