class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        range_list = []
        if len(nums) == 0:
            return range_list

        current_inclusive_list = [nums[0]]
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1]) == 1:
                current_inclusive_list.append(nums[i])
            else:
                range_list.append(current_inclusive_list)
                current_inclusive_list = [nums[i]]
        
        range_list.append(current_inclusive_list)

        final_answer_list = []
        for i in range(0, len(range_list)):
            a = range_list[i][0]
            b = range_list[i][-1]

            if a != b:
                inclusive_list_string = str(a) + "->" + str(b)
            else:
                inclusive_list_string = str(a)
            final_answer_list.append(inclusive_list_string)
        return final_answer_list

