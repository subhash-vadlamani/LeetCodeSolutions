class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_so_far = float('-inf')
        
        curr_sum = 0
        
        for i in range(0, len(nums)):
            if curr_sum < 0 and nums[i] > curr_sum:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            
            if curr_sum > max_so_far:
                max_so_far = curr_sum
        return max_so_far
        