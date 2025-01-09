class Solution:
    def countSubstrings(self, s: str) -> int:
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
        
        palindrome_count = 0
        for i in range(N):
            for j in range(i, N):
                if solve(dp, i, j):
                    palindrome_count += 1
        return palindrome_count