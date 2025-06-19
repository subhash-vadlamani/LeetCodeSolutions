import bisect
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
            [1, 2, 3, 5, 6]
        """

        nums.sort()

        min_subsequence_count = 0
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            current_min_number = nums[i]
            i = bisect.bisect_right(nums, k + current_min_number)
            min_subsequence_count += 1
            # while j >= i:
            #     current_difference = nums[j] - current_min_number
            #     if current_difference > k:
            #         j -= 1
            #     else:
            #         i = j + 1
            #         j = len(nums) - 1
            #         min_subsequence_count += 1
            #         break
        
        return min_subsequence_count
            
        