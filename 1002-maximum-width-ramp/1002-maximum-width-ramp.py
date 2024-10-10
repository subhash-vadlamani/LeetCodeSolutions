class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        """
            Need to find the list that contains maximum element to the 
            right of the current element
        """
        nums_length = len(nums)

        max_right_list = [0] * nums_length
        i = nums_length - 1
        prev_max = 0

        for n in reversed(nums):
            max_right_list[i] = max(nums[i], prev_max)
            prev_max = max_right_list[i]
            i -= 1
        
        l = 0
        # r = 1
        current_answer = 0

        # print(max_right_list)

        for r in range(nums_length):
            # left_number = nums[l]
            # right_number = nums[r]

            while nums[l] > max_right_list[r]:
                l += 1
            current_answer = max(current_answer, r - l)
        return current_answer
            



        