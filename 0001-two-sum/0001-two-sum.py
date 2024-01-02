class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        element_hash = {}

        for i in range(0, len(nums)):
            current_element = nums[i]

            if current_element not in element_hash:
                element_hash[current_element] = [i]
            else:
                element_hash[current_element].append(i)
        
        for i in range(0, len(nums)):
            required_element = target - nums[i]

            if required_element != nums[i]:
                if required_element in element_hash:
                    required_element_index = element_hash[required_element][0]
                    current_element_index = element_hash[nums[i]][0]
                    answer_list = []
                    answer_list.append(required_element_index)
                    answer_list.append(current_element_index)
                    return answer_list
            else:
                if len(element_hash[required_element]) > 1:
                    required_element_index = element_hash[required_element][0]
                    current_element_index = element_hash[required_element][1]
            
                    answer_list = []
                    answer_list.append(required_element_index)
                    answer_list.append(current_element_index)
                    return answer_list




        