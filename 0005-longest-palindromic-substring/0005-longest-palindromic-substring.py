class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len == 0:
            return ""

        dp = [[False] * s_len for _ in range(s_len)]
        max_len = 0
        max_len_string = ""

        for i in range(s_len - 1, -1, -1):  # reverse order
            for j in range(i, s_len):  # forward order
                if s[i] == s[j]:
                    if j - i < 3 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        current_len = j - i + 1
                        if current_len > max_len:
                            max_len = current_len
                            max_len_string = s[i:j + 1]

        return max_len_string
