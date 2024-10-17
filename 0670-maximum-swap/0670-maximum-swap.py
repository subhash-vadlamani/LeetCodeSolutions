class Solution:
    def maximumSwap(self, num: int) -> int:
        num_string = str(num)
        num_string_length = len(num_string)
        next_greater_digit_index = [-1] * num_string_length

        if num_string_length == 1:
            return num

        for i in range(num_string_length - 2, -1, -1):
            if next_greater_digit_index[i + 1] == -1:
                if not (int(num_string[i]) > int(num_string[i + 1])):
                    next_greater_digit_index[i] = i + 1
            else:
                current_next_greater_digit_index = next_greater_digit_index[i + 1]
                current_next_greater_digit = int(num_string[current_next_greater_digit_index])

                if not (int(num_string[i]) > current_next_greater_digit):
                    next_greater_digit_index[i] = current_next_greater_digit_index
        
        def swap_characters(s, i, j):
            char_list = list(s)

            char_list[i], char_list[j] = char_list[j], char_list[i]

            return ''.join(char_list)

        for i in range(0, num_string_length):
            current_next_greater_digit_index = next_greater_digit_index[i]
            if current_next_greater_digit_index != -1:
                if int(num_string[i]) != int(num_string[current_next_greater_digit_index]):
                    num_string = swap_characters(num_string, i, current_next_greater_digit_index)
                    break
        
        return int(num_string)

        