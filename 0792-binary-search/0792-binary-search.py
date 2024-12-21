class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            mid_element = nums[mid]
            if mid_element == target:
                return mid
            elif mid_element < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

        