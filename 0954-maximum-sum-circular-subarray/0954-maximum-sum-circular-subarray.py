class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        curMin = 0
        globalMax = nums[0]
        globalMin = nums[0]
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)

            total += n

            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        
        if globalMax < 0:
            return globalMax
        return max(globalMax, total - globalMin)


        