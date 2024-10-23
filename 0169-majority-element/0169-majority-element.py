class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count_element = nums[0]
        element_count_dict = {}
        element_count_dict[max_count_element] = 1

        for i in range(1, len(nums)):
            if nums[i] in element_count_dict:
                element_count_dict[nums[i]] += 1
            
            else:
                element_count_dict[nums[i]] = 1

            if element_count_dict[nums[i]] > element_count_dict[max_count_element]:
                max_count_element = nums[i]
        return max_count_element


