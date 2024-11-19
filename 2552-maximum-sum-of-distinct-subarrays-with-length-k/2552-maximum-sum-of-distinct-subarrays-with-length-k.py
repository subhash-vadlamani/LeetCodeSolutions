class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
            This looks like a sliding window problem.
            The most challenging part of the problem would be
            to know if all the elements of the subarray are distinct.

            maintain a counter 'distinctElementCount' that stores
            the number of distinct elements in the length k. If it is equal to 'k'
            compare the sum with the current max, or else, do not
        """

        l = 0
        current_sum_max = float('-inf')
        current_sum = 0
        distinct_element_count = 0
        element_dict = dict()
        nums_length = len(nums)

        for r in range(nums_length):
            current_element = nums[r]

            if current_element not in element_dict:
                element_dict[current_element] = 1
                distinct_element_count += 1
            else:
                element_dict[current_element] += 1
            
            current_sum += current_element
            
            if r - l + 1 == k:
                if distinct_element_count == k:
                    current_sum_max = max(current_sum_max, current_sum)

                deleted_element = nums[l]

                if element_dict[deleted_element] == 1:
                    element_dict.pop(deleted_element)
                    distinct_element_count -= 1
                else:
                    element_dict[deleted_element] -= 1
                
                current_sum -= deleted_element
                l += 1
        
        return 0 if current_sum_max == float('-inf') else current_sum_max



        