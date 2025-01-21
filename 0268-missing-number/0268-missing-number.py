class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        ans ^= 0
        for i in range(1, len(nums)):
            ans ^= i
            ans ^= nums[i]
        return ans ^ len(nums)
        