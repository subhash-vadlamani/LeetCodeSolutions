class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        temp = float('-inf')

        def safe_get(arr, index, default):
            if 0 <= index < len(arr):
                return arr[index]
            return default

        if n == 1:
            return 0

        while left <= right:
            mid = (left + right) // 2

            if mid == 0 and nums[mid] > safe_get(nums, mid+1, temp):
                return mid
            elif mid == n - 1 and nums[mid] > safe_get(nums, mid-1, temp):
                return mid
            
            if nums[mid] > safe_get(nums, mid-1, temp) and nums[mid] > safe_get(nums, mid+1, temp):
                return mid
            elif nums[mid] > safe_get(nums, mid-1, temp):
                left = mid + 1
            else:
                right = mid - 1
        return mid
                
        