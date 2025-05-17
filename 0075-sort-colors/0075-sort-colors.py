class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_count = 0
        white_count = 0
        blue_count = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                red_count += 1
            elif nums[i] == 1:
                white_count += 1
            else:
                blue_count += 1
        
        i = 0
        for j in range(i, i + red_count):
            nums[j] = 0
        i += red_count
        for j in range(i, i+ white_count):
            nums[j] = 1
        
        i += white_count
        for j in range(i, i + blue_count):
            nums[j] = 2
            
