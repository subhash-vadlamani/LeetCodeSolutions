class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
            convert the list of integers to list of strings 
        """

        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        for i in range(len(nums)):
            new_num = nums[(int(nums[i].split("-")[0]))]
            combined_num = nums[i] + "-" + new_num
            nums[i] = combined_num
        
        for i in range(len(nums)):
            nums[i] = int(nums[i].split("-")[1])
        
        return nums
        