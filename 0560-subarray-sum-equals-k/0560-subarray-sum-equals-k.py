class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        current_prefix_sum = 0
        prefix_sum_hashmap = dict()
        subarray_count = 0

        for i in range(len(nums)):
            current_prefix_sum += nums[i]
            if current_prefix_sum == k:
                subarray_count += 1
            
            # current_prefix_sum - required_previous_prefix_sum = k
            required_previous_prefix_sum = current_prefix_sum - k

            if required_previous_prefix_sum in prefix_sum_hashmap:
                subarray_count += prefix_sum_hashmap[required_previous_prefix_sum]
            
            if current_prefix_sum in prefix_sum_hashmap:
                prefix_sum_hashmap[current_prefix_sum] += 1
            else:
                prefix_sum_hashmap[current_prefix_sum] = 1
        return subarray_count



        