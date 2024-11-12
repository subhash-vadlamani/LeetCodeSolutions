class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = float('inf')
        l = 0
        current_sum = 0
        nums_length = len(nums)

        for r in range(nums_length):
            current_sum += nums[r]

            while current_sum >= target:
                current_length = r - l + 1
                min_length = min(min_length, current_length)
                current_sum -= nums[l]
                l += 1
        
        return 0 if min_length == float('inf') else min_length




        