class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[0 for _ in range(N)] for _ in range(N)]

        def solve(dp, i, j):

            if i > j:
                # dp[i][j] = True
                return True

            if dp[i][j] != 0:
                return dp[i][j]
            
            if s[i] == s[j]:
                if i + 1 > j  - 1 or solve(dp, i + 1, j - 1):
                    dp[i][j] = True
                    return True
                
            dp[i][j] = False
            return False
        
        max_len = 0
        start_index = 0
        for i in range(N):
            for j in range(i + max_len, N):
                if j - i + 1 > max_len and solve(dp, i, j):
                    max_len = j - i + 1
                    start_index = i
        print(max_len)
        return s[start_index:start_index+max_len]

        