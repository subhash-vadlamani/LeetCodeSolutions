from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minK_index = -1
        maxK_index = -1
        bad_index = -1
        count = 0

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_index = i
            
            if num == minK:
                minK_index = i
            if num == maxK:
                maxK_index = i
            
            min_valid = min(minK_index, maxK_index)
            if min_valid > bad_index:
                count += min_valid - bad_index

        return count
