class Solution:
    def makeFancyString(self, s: str) -> str:
        
        s_len = len(s)
        previous_character= None
        previous_count = 0

        string_list = list(s)

        for i in range(s_len):
            current_character = string_list[i]
            if previous_character == current_character and previous_count == 2:
                string_list[i] = '#'
            elif previous_character == current_character:
                previous_count += 1
            else:
                previous_character = string_list[i]
                previous_count = 1
        
        new_string = ""
        for i in range(s_len):
            if string_list[i] != '#':
                new_string += str(string_list[i])
        return new_string

