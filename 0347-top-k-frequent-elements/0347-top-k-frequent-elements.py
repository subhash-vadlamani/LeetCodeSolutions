class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count_dict = dict()

        for num in nums:
            if num in nums_count_dict:
                nums_count_dict[num] += 1
            else:
                nums_count_dict[num] = 1
        
        sorted_keys = sorted(nums_count_dict, key = lambda k:nums_count_dict[k], reverse = True)

        return sorted_keys[:k]
        