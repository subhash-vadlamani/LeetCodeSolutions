class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # sliding window of fixed size

        i = 0
        j = 2

        subarray_count = 0

        while j < len(nums):
            if (nums[i] + nums[j]) == nums[(i + j) // 2] / 2:
                subarray_count +=1
            
            i += 1
            j += 1
        
        return subarray_count
        