class Solution:
    """
    You are given a string s.

    Consider performing the following operation until s becomes empty:

        - For every alphabet character from 'a' to 'z', remove the first occurrence of that character in s (if it exists).

    Return the value of the string s right before applying the last operation.

    Example 1:

    ```
    Input: s = "aabcbbca"
    Output: "ba"
    Explanation: We do the following operations:
    - Remove the underlined characters s = "aabcbbca". The resulting string is s = "abbca".
    - Remove the underlined characters s = "abbca". The resulting string is s = "ba".
    - Remove the underlined characters s = "ba". The resulting string is s = "".
    The string just before the last operation is "ba".
    ```

    Example 2:

    ```
    Input: s = "abcd"
    Output: "abcd"
    Explanation: We do the following operation:
    - Remove the underlined characters s = "abcd". The resulting string is s = "".
    The string just before the last operation is "abcd".
    ```
    """

    def lastNonEmptyString(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1
        most = max(cnt)

        res = ""
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1
            if cnt[ord(c) - ord("a")] == most:
                res += c

        return res
