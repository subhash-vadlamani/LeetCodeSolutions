class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        dp = defaultdict(int)

        dp[0] = 1 # (0 sum) -> 1 way

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp
        return dp[target]

        # dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        # dp[0][0] = 1 # (0 elements, 0 sum) -> 1 way

        # for i in range(len(nums)):
        #     for cur_sum, count in dp[i].items():
        #         dp[i + 1][cur_sum + nums[i]] += count
        #         dp[i + 1][cur_sum - nums[i]] += count
        # return dp[len(nums)][target]


        # cache = {}

        # def dfs(i, current_sum):
        #     if i == len(nums):
        #         if current_sum == target:
        #             return 1
        #         return 0
        #     if (i, current_sum) in cache:
        #         return cache[(i, current_sum)]
            
        #     cache[(i, current_sum)] = dfs(i + 1, current_sum + nums[i]) + dfs(i + 1, current_sum - nums[i])
        #     return cache[(i, current_sum)]
        # return dfs(0, 0)
        