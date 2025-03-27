from collections import defaultdict
import math
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        element_frequency_dict = defaultdict(int)

        for num in nums:
            element_frequency_dict[num] += 1
        
        # print(element_frequency_dict)
        # find the dominent element
        dom_element_value = 0
        dom_element_freq = float('-inf')

        for element, element_freq in element_frequency_dict.items():
            if element_freq > dom_element_freq:
                dom_element_value = element
                dom_element_freq = element_freq
        
        # print(f'the dom element is {dom_element_value} and its frequency is {dom_element_freq}')
        
        # we found the dom element and it's frequency
        n = len(nums)
        left_subarray_dom_element_freq = 0

        for i in range(n - 1):
            """
                Considering the following subarrays
                nums[0, ....., i] and nums[i + 1, ...., n - 1] (indices inculsive)
            """
            if nums[i] == dom_element_value:
                left_subarray_dom_element_freq += 1
            
            right_subarray_dom_element_freq = dom_element_freq - left_subarray_dom_element_freq

            """
                i + 1 + k = n. => k = n - (i + 1)
            """


            left_subarray_length = i + 1
            right_subarray_length = n - (i + 1)

            # print(f"i is {i}. left subarray dom element freq is {left_subarray_dom_element_freq}. right subarray dom element freq is {right_subarray_dom_element_freq}")

            # check if the dom element is the dom element of both the subarrays

            if (left_subarray_dom_element_freq > int(math.floor(left_subarray_length / 2))) and (
                right_subarray_dom_element_freq > int(math.floor(right_subarray_length / 2))
            ):
                return i
        
        return - 1
        

        