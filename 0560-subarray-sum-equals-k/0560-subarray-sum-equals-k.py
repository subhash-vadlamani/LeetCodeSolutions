class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        prev_dict = dict()
        prev_dict[0] = 1
        subarray_count = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            # we are looking for prev prefix sums of the value (prefix_sum - k)

            subarray_count += prev_dict.get(prefix_sum - k, 0)

            prev_dict[prefix_sum] = 1 + prev_dict.get(prefix_sum, 0)
        
        return subarray_count
        
        