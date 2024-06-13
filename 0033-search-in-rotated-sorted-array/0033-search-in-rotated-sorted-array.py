class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        def find_rotation_index(nums):


            if nums[0] <= nums[-1]:
                return 0
            
            i = 0
            j = len(nums) - 1

            while i <= j:
                k = (i+j) // 2

                current_number = nums[k]
                if current_number > nums[k + 1]:
                    return k + 1
                elif current_number < nums[0]:
                    j = k - 1
                else:
                    i = k + 1

            return 0

        def perform_binary_search(nums, i, j, target):

            while i <= j:
                k = (i + j) // 2

                current_number = nums[k]

                if target == current_number:
                    return k
                elif target > current_number:
                    i = k + 1
                else:
                    j = k - 1
            
            return - 1

        rotation_index = find_rotation_index(nums)

        if nums[rotation_index] <= target <= nums[-1]:
            return perform_binary_search(nums, rotation_index, len(nums) - 1, target)
        else:
            return perform_binary_search(nums, 0, rotation_index - 1, target)

        # if current_rotation_index == 0:
        #     return perform_binary_search(nums, 0, len(nums) - 1, target)
        # else:
        #     if target < nums[0]:
        #         return perform_binary_search(nums, current_rotation_index + 1, len(nums) - 1, target)
            
        #     elif target > nums[0]:
        #         return perform_binary_search(nums, 0, current_rotation_index - 1, target)
        #     else:
        #         return 0
        





        