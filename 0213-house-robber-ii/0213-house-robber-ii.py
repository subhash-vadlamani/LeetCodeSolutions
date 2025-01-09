class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            N = len(houses)

            if N == 0:
                return 0
            if N == 1 or N == 2:
                return max(houses)

            dp = [0] * N
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, N):
                dp[i] = max((houses[i] + dp[i - 2]), dp[i - 1])
            return dp[-1]
        
        nums_len = len(nums)
        if nums_len == 1:
            return max(nums)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))