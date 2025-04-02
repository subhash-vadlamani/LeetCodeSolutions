class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        current_max = float('-inf')

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    current_max = max(current_max, (nums[i] - nums[j]) * nums[k])
        
        if current_max < 0:
            return 0
        return current_max
        