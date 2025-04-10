from collections import defaultdict
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        """
            dict to maintain the frequency of each element
        """

        """
            eg1: [5, 2, 5, 4, 5]

        """

        count_dict = defaultdict(int)
        min_key = float('inf')

        for num in nums:
            count_dict[num] += 1
            if num < min_key:
                min_key = num
        
        # sorted_count_dict_keys = sorted(count_dict.keys(), reverse = True)
        count_dict_keys = count_dict.keys()
        count_dict_keys_length = len(count_dict_keys)

        """
            sorted_count_dict_keys : [5, 4, 2]

            the value of k should either be less than the minimum element or equal to it
        """

        if k > min_key:
            return - 1
        elif k == min_key:
            return count_dict_keys_length - 1
        else:
            return count_dict_keys_length
        
            

        