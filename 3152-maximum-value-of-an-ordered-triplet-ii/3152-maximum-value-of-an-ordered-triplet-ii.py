class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix_max = [0] * len(nums)
        suffix_max = [0] * len(nums)

        prefix_max[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
        
        suffix_max[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i+ 1], nums[i])
        
        current_max = 0

        for i in range(len(nums)):
            if (i - 1) < 0 or (i + 1) > len(nums) - 1:
                continue
            current_max = max(current_max, (prefix_max[i - 1] - nums[i]) * suffix_max[i + 1])
        return current_max
        