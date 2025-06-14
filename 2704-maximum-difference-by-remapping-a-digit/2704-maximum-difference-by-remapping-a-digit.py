class Solution:
    def minMaxDifference(self, num: int) -> int:
        """
            for min -> first non-zero number to zero
            for max -> first non-nine number to nine
        """
        num_string = str(num)
        min_ch_digit_to_replace = -1
        max_ch_digit_to_replace = -1
        

        for ch in num_string:
            # current_digit = int(ch)
            if ch != '0' and min_ch_digit_to_replace == -1:
                min_ch_digit_to_replace = ch
            
            if ch != '9' and max_ch_digit_to_replace == -1:
                max_ch_digit_to_replace = ch

                
        
        min_num_string_list = []
        max_num_string_list = []

        for ch in num_string:
            # current_digit = int(ch)

            if ch == min_ch_digit_to_replace:
                if min_num_string_list:
                    min_num_string_list.append('0')
            else:
                min_num_string_list.append(ch)
        
        for ch in num_string:

            if ch == max_ch_digit_to_replace:
                max_num_string_list.append('9')
            else:
                max_num_string_list.append(ch)
        # print(max_num_string_list)


        max_number = int("".join(max_num_string_list))

        if not min_num_string_list:
            min_number = 0
        else:
            min_number = int("".join(min_num_string_list))
        
        return max_number - min_number
        

        