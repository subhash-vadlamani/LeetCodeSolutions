class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        """
            Initialize the dp array as the same dimensions of the triangle
        """
        n = len(triangle)
        m = len(triangle[-1])
        """
            n -> Number of rows in the triangle
            m -> maximum number of columns in a triangle
        """
        dp = []
        for i in range(n):
            current_list = [float('inf')] * (i + 1)
            dp.append(current_list)
        
        dp[0][0] = triangle[0][0]
        # print(dp)

        for i in range(1, n):
            for j in range(0, i + 1):
                # print("({}, {})".format(i-1, j))
                if j <= i - 1:
                    choice1 = dp[i-1][j]
                else:
                    choice1 = float('inf')
                if j - 1 >= 0:
                    choice2 = dp[i-1][j-1]
                else:
                    choice2 = float('inf')
                dp[i][j] = min(choice1, choice2) + triangle[i][j]
        
        dp_last_row = dp[-1]
        return min(dp_last_row)


        