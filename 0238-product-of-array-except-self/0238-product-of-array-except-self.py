class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)

        # prefix_list = [1] * nums_length
        answer_list = [1] * nums_length

        for i in range(nums_length-2, -1, -1):
            answer_list[i] = answer_list[i+1] * nums[i+1]

        temp1 = temp2 = 1
        for i in range(1, nums_length):
            temp2 = nums[i]
            nums[i] = nums[i-1] * temp1
            temp1 = temp2
            # prefix_list[i] = prefix_list[i-1] * nums[i - 1]
        nums[0] = 1
        # print()
        
        # answer_list = []
        for i in range(nums_length):
            answer_list[i] *= nums[i]
        return answer_list
        