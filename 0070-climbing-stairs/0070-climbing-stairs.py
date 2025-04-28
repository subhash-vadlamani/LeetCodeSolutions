class Solution:
    def climbStairs(self, n: int) -> int:

        """
            DP road map

            Recursion -> Memoization -> True DP
        """

        # recursive solution -> TLE

        # def dfs(i):
        #     """
        #         Number of ways to reach the top from index i
        #     """
        #     if i > n:
        #         return 0
        #     elif i == n:
        #         return 1
        #     else:
        #         return dfs(i + 1) + dfs(i + 2)


        
        
        # return dfs(0)


        # Memoization

        memo = dict()

        def dfs(i):
            if i > n:
                return 0
            elif i == n:
                return 1
            
            if (i + 1) in memo:
                val1 = memo[i + 1]
            else:
                val1 = dfs(i + 1)
            

            if (i + 2) in memo:
                val2 = memo[i + 2]
            else:
                val2 = dfs(i + 2)
            
            val3 = val1 + val2
            memo[i] = val3
            return val3
        
        return dfs(0)
        