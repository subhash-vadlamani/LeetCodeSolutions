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

        for num in nums:
            count_dict[num] += 1
        
        sorted_count_dict_keys = sorted(count_dict.keys(), reverse = True)

        """
            sorted_count_dict_keys : [5, 4, 2]

            the value of k should either be less than the minimum element or equal to it
        """

        if k > sorted_count_dict_keys[-1]:
            return - 1
        elif k == sorted_count_dict_keys[-1]:
            return len(sorted_count_dict_keys) - 1
        else:
            return len(sorted_count_dict_keys)
        
            

        