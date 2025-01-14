class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum > current_max:
                current_max = current_sum
            if current_sum < 0:
                current_sum = 0
        return current_max
        