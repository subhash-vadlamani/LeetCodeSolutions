class Solution:
    def minimumSteps(self, s: str) -> int:

        """
            We maintain a list to store the number of one's before a particular
            index
        """
        string_length = len(s)

        ones_before_list = [0] * string_length
        current_one_count = 0

        for i in range(0, string_length):
            ones_before_list[i] = current_one_count
            if s[i] == '1':
                current_one_count += 1
        
        min_swaps_required = 0

        for i in range(0, string_length):
            if s[i] == '0':
                min_swaps_required += ones_before_list[i]
        return min_swaps_required
        