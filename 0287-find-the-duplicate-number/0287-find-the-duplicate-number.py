class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Cyclic Sort

        """
            If the value is 'val', the correct index is 'val - 1'
        """

        i = 0
        nums_len = len(nums)

        while i < nums_len:
            current_val = nums[i]
            current_val_correct_index = current_val - 1

            if nums[i] != nums[current_val_correct_index]:
                nums[i], nums[current_val_correct_index] = nums[current_val_correct_index], nums[i]
            else:
                i += 1
        
        for j in range(nums_len):
            if nums[j] != j + 1:
                return nums[j]
        
        