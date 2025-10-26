from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Use a single binary search function that takes a boolean
        indicating if we are searching for the leftmost or rightmost index.
        """

        def perform_search(start, end, searchLeft):
            result = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    result = mid
                    if searchLeft:
                        end = mid - 1   # keep searching left side
                    else:
                        start = mid + 1 # keep searching right side
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return result

        if not nums:
            return [-1, -1]

        left = perform_search(0, len(nums) - 1, True)
        right = perform_search(0, len(nums) - 1, False)
        return [left, right]
