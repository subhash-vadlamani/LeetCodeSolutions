class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        current_max = float('-inf')

        for i in range(1, len(nums)):
            current_max = max(current_max, abs(nums[i] - nums[i-1]))
        

        # first and last element check
        current_max = max(current_max, abs(nums[0] - nums[-1]))
        return current_max