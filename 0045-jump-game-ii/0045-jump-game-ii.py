class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            current_jumps = nums[i]
            current_minimum = float('inf')

            for j in range(current_jumps, 0, -1):
                if i + j < len(nums):
                    current_minimum = min(current_minimum, dp[i + j])
            dp[i] = 1 + current_minimum
        return dp[0]