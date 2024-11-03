class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            2D DP question.
            m = len(grid)
            n = len(grid[0])
            Intial position: (0,0)
            Final Position: (m, n)
            Movement : if at (i, j), we have two choices:
                1. (i, j+1)
                2. (i+1, j)
        """

        """
            Initialize the DP array
        """
        m = len(grid)
        n = len(grid[0])

        def indicesInbound(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            else:
                return False

        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        # print(dp)

        for i in range(m):
            for j in range(n):
                """
                    current location : (i, j)
                    It can be reached from (i, j-1), (i-1, j)
                """
                if i == 0 and j == 0:
                    continue

                if indicesInbound(i, j-1):
                    choice1 = dp[i][j-1]
                else:
                    choice1 = float('inf')
                
                if indicesInbound(i-1, j):
                    choice2 = dp[i-1][j]
                else:
                    choice2 = float('inf')
                

                dp[i][j] = min(choice1, choice2) + grid[i][j]
        
        # print(dp)
        return dp[m-1][n-1]


        