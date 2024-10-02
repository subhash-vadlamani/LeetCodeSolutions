class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        duplicate_arr = arr[:]

        sorted_duplicate_arr = sorted(duplicate_arr)
        unique_sorted_duplicate_arr = list(dict.fromkeys(sorted_duplicate_arr))

        rank_dict = dict()

        for i in range(0, len(unique_sorted_duplicate_arr)):
            rank_dict[unique_sorted_duplicate_arr[i]] = i + 1
        
        for i in range(0, len(arr)):
            arr[i] = rank_dict[arr[i]]
        
        return arr
        