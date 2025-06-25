class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {} # (i, j)
        s_len = len(s)
        t_len = len(t)

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == t_len:
                return 1
            
            if i == s_len:
                return 0

            if s[i] == t[j]:
                # we can pick the character at s[i] or not

                count = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                count = dfs(i + 1, j)
            
            memo[(i, j)] = count
            return count
        
        return dfs(0, 0)
        