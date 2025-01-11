class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        """
            Step 1: Initialize the DP matrix
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1
        """
            Step 2 : Start from last column and last row
            and go in reverse.
        """
        directions = [(1, 0), (0, 1)]
        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                for di, dj in directions:
                    new_i, new_j = i + di, j + dj
                    if new_i in range(m) and new_j in range(n):
                        dp[i][j] += dp[new_i][new_j]
        return dp[0][0]
        