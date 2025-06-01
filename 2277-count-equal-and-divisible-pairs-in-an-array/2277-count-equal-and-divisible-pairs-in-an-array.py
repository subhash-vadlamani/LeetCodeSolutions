from collections import defaultdict
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        # index_dict = defaultdict(list) # key is the number, value is the index list

        # for i in range(len(nums)):
        #     index_dict[nums[i]].append(i)

        num_pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] == nums[j]) and ((i * j) % k == 0):
                    num_pairs += 1
        
        return num_pairs
        
        



        