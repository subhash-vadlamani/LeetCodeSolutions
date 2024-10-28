class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]* n for _ in range(m)]
        max_square_size = float('-inf')

        for i in range(0, m):
            for j in range(0, n):

                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    if max_square_size < dp[i][j]:
                        max_square_size = dp[i][j]
        
        if max_square_size < 0:
            return 0
        else:
            return max_square_size ** 2



        