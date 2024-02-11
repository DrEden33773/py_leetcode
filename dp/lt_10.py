class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 预处理一下
        pattern = []
        for c in p:
            if c == "*":
                pattern[-1] += c
            else:
                pattern.append(c)
        # dp[i][j] 表示 pattern[:i] 和 s[:j] 是否匹配
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(pattern) + 1)]
        # 空 pattern 和 '' 匹配
        dp[0][0] = 1

        for i, pat in enumerate(pattern, 1):
            # 无通配符匹配
            if len(pat) == 1:
                for j, c in enumerate(s, 1):
                    if pat == "." or pat == c:
                        dp[i][j] = dp[i - 1][j - 1]
            else:
                # ".*" matches anything
                if pat[0] == ".":
                    #  使用 0 次
                    dp[i][0] = dp[i - 1][0]
                    for j in range(1, len(s) + 1):
                        # dp[i-1][j] 使用 0次
                        # dp[i-1][j-1] 使用1 次
                        # dp[i][j-1] 使用第N次
                        maxP = max([dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]])
                        dp[i][j] = maxP
                else:
                    # "a*" like, matches if s[j] == 'a'
                    dp[i][0] = dp[i - 1][0]
                    for j, c in enumerate(s, 1):
                        # 0 次
                        dp[i][j] = dp[i - 1][j]
                        # 匹配的情况下，使用看看
                        if pat[0] == c:
                            dp[i][j] = max([dp[i][j], dp[i - 1][j - 1], dp[i][j - 1]])
        return bool(dp[-1][-1])
