class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_array_value = -1

        for i in range(0, len(nums)):
            if nums[i] > max_array_value:
                max_array_value = nums[i]

        max_subarray_length = 0
        current_subarray_length = 0
        for i in range(0, len(nums)):
            if nums[i] == max_array_value:
                current_subarray_length += 1
            else:
                if current_subarray_length > max_subarray_length:
                    max_subarray_length = current_subarray_length
                current_subarray_length = 0
        
        if current_subarray_length > max_subarray_length:
            max_subarray_length = current_subarray_length
        return max_subarray_length


        # max_bitwise_and = -1
        # max_subarray_length = -1

        # for i in range(0, len(nums)):
        #     current_bitwise_and = nums[i]
        #     for j in range(i, len(nums)):
        #         current_bitwise_and = current_bitwise_and & nums[j]
        #         current_subarray_length = j - i + 1
        #         if current_bitwise_and == max_bitwise_and:
        #             if current_subarray_length > max_subarray_length:
        #                 max_subarray_length = current_subarray_length
        #         elif current_bitwise_and > max_bitwise_and:
        #             max_bitwise_and = current_bitwise_and
        #             max_subarray_length = current_subarray_length
        # return max_subarray_length

        