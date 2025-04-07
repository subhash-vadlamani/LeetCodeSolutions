class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        memo = {}

        def dfs(i, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target or i == len(nums):
                return False
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            memo[(i, curr_sum)] = dfs(i + 1, curr_sum + nums[i]) or dfs(i + 1, curr_sum)
            return memo[(i, curr_sum)]

        return dfs(0, 0)
