class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
            sliding window
            variable length sliding window
        """
        l = 0
        r = 0
        current_sum = 0
        max_sum = float('-inf')
        nums_set = set()

        while r < len(nums):
            if nums[r] not in nums_set:
                nums_set.add(nums[r])
                current_sum += nums[r]
                r += 1
            else:
                max_sum = max(max_sum, current_sum)
                nums_set.remove(nums[l])
                current_sum -= nums[l]
                l += 1
        
        max_sum = max(max_sum, current_sum)
        return max_sum
            

        