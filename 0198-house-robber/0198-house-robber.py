class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_length = len(nums)
        dp = [0] * (nums_length + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, nums_length + 1):
            dp[i] = max((nums[i - 1] + dp[i - 2]), dp[i - 1])
        return dp[-1]
        