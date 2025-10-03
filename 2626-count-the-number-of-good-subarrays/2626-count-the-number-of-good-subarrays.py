from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        good_subarray_count = 0
        l = 0
        r = 0
        number_dict = defaultdict(int)
        nums_len = len(nums)
        current_pairs = 0

        while r < nums_len:
            current_pairs += number_dict[nums[r]]
            number_dict[nums[r]] += 1
            while current_pairs >= k:
                good_subarray_count += (nums_len - r)
                number_dict[nums[l]] -= 1
                current_pairs -= (number_dict[nums[l]])
                l += 1
            r += 1
        return good_subarray_count





        