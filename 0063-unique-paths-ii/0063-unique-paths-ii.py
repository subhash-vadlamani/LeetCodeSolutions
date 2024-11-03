class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]* n for _ in range(m)]

        def considerIndices(i, j):
            if 0 <= i < m and 0 <= j < n and obstacleGrid[i][j] == 0:
                return True
            else:
                return False
        
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or obstacleGrid[i][j] == 1:
                    continue
                
                """
                    the current index (i, j) can be reached from 2 positions:
                        1. (i, j-1)
                        2. (i-1, j)
                """

                if considerIndices(i, j-1):
                    choice1 = dp[i][j-1]
                else:
                    choice1 = 0
                
                if considerIndices(i-1, j):
                    choice2 = dp[i-1][j]
                else:
                    choice2 = 0
                
                dp[i][j] = choice1 + choice2
        
        return dp[m-1][n-1]
        