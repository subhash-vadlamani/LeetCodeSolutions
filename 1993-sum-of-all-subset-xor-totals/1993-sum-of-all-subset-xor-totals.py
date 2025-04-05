class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        N = len(nums)
        for num in nums:
            result |= num
        
        return result << (N - 1)
        