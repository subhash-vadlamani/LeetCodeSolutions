class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)

        prefix_list = [1] * nums_length
        suffix_list = [1] * nums_length

        for i in range(1, nums_length):
            prefix_list[i] = prefix_list[i-1] * nums[i - 1]
        
        for i in range(nums_length-2, -1, -1):
            suffix_list[i] = suffix_list[i+1] * nums[i+1]
        
        answer_list = []
        for i in range(nums_length):
            answer_list.append(prefix_list[i] * suffix_list[i])
        return answer_list
        