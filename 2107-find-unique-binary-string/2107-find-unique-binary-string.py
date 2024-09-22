class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        def binary_to_decimal(binary_string):
            reversed_binary_string = binary_string[::-1]
            current_multiplier = 1
            current_decimal_number = 0

            for char in reversed_binary_string:
                current_binary_digit = int(char)

                current_decimal_number += (current_multiplier * current_binary_digit)
                current_multiplier *= 2
            return current_decimal_number
            
        
        def decimal_to_binary(decimal_num, nums):
            current_binary_string = ""
            nums_length = len(nums)
            if decimal_num == 0:
                return ("0" * nums_length)

            while decimal_num:
                current_char = str(decimal_num % 2)
                current_binary_string += current_char
                decimal_num = decimal_num // 2
            print(current_binary_string)
            final_binary_string = current_binary_string[::-1]
            final_binary_string_length = len(final_binary_string)
            if final_binary_string_length < nums_length:
                length_diff = nums_length - final_binary_string_length
                final_binary_string = "0" * length_diff + final_binary_string
            return final_binary_string
        
        nums_length = len(nums)

        string_presence_list = [0 for _ in range(0, 2 ** nums_length)]
        # print(string_presence_list)

        for num in nums:
            decimal_num = binary_to_decimal(num)
            # print(decimal_num)
            string_presence_list[decimal_num] = 1
        for i in range(0, len(string_presence_list)):
            if string_presence_list[i] == 0:
                required_decimal_num = i
                break
        
        required_binary_string = decimal_to_binary(required_decimal_num, nums)
        return required_binary_string