class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
            We are going to be constructing a dp array.
            In the dp array, dp[i] is going to represent the 
            minimum cost to pay to leave the ith step
        """

        def construct_dp(cost):
            number_of_stairs = len(cost)
            dp = [0] * number_of_stairs

            dp[0] = cost[0]
            dp[1] = cost[1]

            for i in range(2, number_of_stairs):
                dp[i] = min(dp[i-1], dp[i - 2]) + cost[i]
            return dp
        
        dp = construct_dp(cost)
        # print(dp)

        return min(dp[-1], dp[-2])

        