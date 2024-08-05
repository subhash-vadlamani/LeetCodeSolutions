class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        string_count_dict = dict()

        for i in range(0, len(arr)):
            if arr[i] not in string_count_dict:
                string_count_dict[arr[i]] = 1
            else:
                string_count_dict[arr[i]] += 1
        
        current_distinct_string_count = 0
        for i in range(0, len(arr)):
            if string_count_dict[arr[i]] == 1:
                current_distinct_string_count += 1
            
            if current_distinct_string_count == k:
                return arr[i]
        return ""

        