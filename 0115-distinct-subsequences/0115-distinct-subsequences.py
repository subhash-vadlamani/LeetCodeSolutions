class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        s_len = len(s)
        t_len = len(t)

        dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]

        for i in range(s_len + 1):
            dp[i][t_len] = 1

        for i in range(s_len - 1, -1, -1):
            for j in range(t_len - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        
        return dp[0][0]




        # memo = {} # (i, j)
        # s_len = len(s)
        # t_len = len(t)

        # def dfs(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
            
        #     if j == t_len:
        #         return 1
            
        #     if i == s_len:
        #         return 0

        #     if s[i] == t[j]:
        #         # we can pick the character at s[i] or not

        #         count = dfs(i + 1, j + 1) + dfs(i + 1, j)
        #     else:
        #         count = dfs(i + 1, j)
            
        #     memo[(i, j)] = count
        #     return count
        
        # return dfs(0, 0)
        