class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
            we can flip at most k 0's
            we need to find the maximum window with consecutive 1's
            varible window problem
        """
        l = 0
        r = 0
        max_len = float('-inf')

        while r < len(nums):
            if nums[r] == 1:
                r += 1
            else:
                if k:
                    k -= 1
                    r += 1
                else:
                    max_len = max(max_len, r - l)
                    if nums[l] == 0:
                        k += 1
                    l += 1
        
        max_len = max(max_len, r - l)
        return max_len

        