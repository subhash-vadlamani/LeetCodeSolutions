class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # step1: Sort the list
        nums.sort()
        nums_len = len(nums)
        l = 0
        r = 0
        max_freq = float('-inf')
        total = 0

        while r < nums_len:
            total += nums[r]

            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            
            max_freq = max(max_freq, (r - l + 1))
            r += 1
        return max_freq


       