class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_dict = dict()

        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        
        current_max = -1

        for key in num_dict.keys():
            if num_dict[key] == 1:
                if key > current_max:
                    current_max = key
        return current_max