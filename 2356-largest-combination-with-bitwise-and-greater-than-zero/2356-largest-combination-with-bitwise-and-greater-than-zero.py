class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        """
            Brute Force would involve looking at all the (2 ** n) combinations.
            This is not viable.
        """

        binary_string_list = []

        for candidate in candidates:
            binary_string_list.append(bin(candidate)[2:].zfill(24))
        
        non_zero_bit_count_list = []

        for i in range(24):
            count = 0
            for binary_string in binary_string_list:
                if binary_string[i] == '1':
                    count += 1
            non_zero_bit_count_list.append(count)
        
        return max(non_zero_bit_count_list)
        