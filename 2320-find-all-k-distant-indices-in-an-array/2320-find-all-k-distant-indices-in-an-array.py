class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
            Iterate over the list, find the indices where the value is key.
            for each of that indice, add the range of elements into a set and convert that
            to a list
        """
        
        key_index_list = []
        answer_set = set()
        for i in range(len(nums)):
            if nums[i] == key:
                key_index_list.append(i)
        
        for index in key_index_list:
            for i in range(index - k, index + k + 1):
                if i in range(len(nums)):
                    answer_set.add(i)
        
        return sorted(list(answer_set))
        
