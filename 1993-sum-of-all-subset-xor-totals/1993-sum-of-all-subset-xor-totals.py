class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset_list = []
        nums_length = len(nums)

        def calculate_subset(current_subset, index):
            if index == nums_length:
                subset_list.append(current_subset)
                return
            
            calculate_subset(current_subset + [nums[index]], index + 1)
            calculate_subset(current_subset, index + 1)
        
        calculate_subset([], 0)

        def calculate_list_xor(my_list):
            if not my_list:
                return 0
            
            xor_value = my_list[0]
            for i in range(1, len(my_list)):
                xor_value ^= my_list[i]
            return xor_value

        answer = 0
        # print(subset_list)
        for subset in subset_list:
            answer += calculate_list_xor(subset)
        
        return answer


        