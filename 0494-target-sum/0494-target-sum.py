class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {}

        def dfs(i, current_sum):
            if i == len(nums):
                if current_sum == target:
                    return 1
                return 0
            if (i, current_sum) in cache:
                return cache[(i, current_sum)]
            
            cache[(i, current_sum)] = dfs(i + 1, current_sum + nums[i]) + dfs(i + 1, current_sum - nums[i])
            return cache[(i, current_sum)]
        return dfs(0, 0)
        