class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        number_frequency = dict()

        for num in nums:
            if num not in number_frequency:
                number_frequency[num] = 1
            else:
                number_frequency[num] += 1
        # current_arr = sorted(arr)
        sorted_arr = sorted(nums, key = lambda x: (number_frequency[x], -x))
        return sorted_arr
        