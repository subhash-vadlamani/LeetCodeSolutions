class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1, -1]
        
        
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        
        
        
        while left < len(nums) and nums[left] != target:
            left += 1
        while right >= 0 and nums[right] != target :
            right -= 1
        
        if left == len(nums):
            left = -1
        
        return [left, right]
        