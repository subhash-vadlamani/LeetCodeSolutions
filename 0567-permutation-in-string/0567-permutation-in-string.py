class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def compute_character_dict_list(s, required_substring_length):
            """
                Compute all the substrings of the required length and also
                store the mapping of the count of each and every character
                in a dictionary.
            """

            """
                First, we compute all the substrings of the given length
            """

            i = 0
            j = required_substring_length
            given_string_length = len(s)
            substring_list = []

            while j <= given_string_length:
                current_substring = s[i:j]
                substring_list.append(current_substring)
                i += 1
                j += 1
            
            """
                Now that we have the list of substrings, we make a 
                list of dicts where each dict contains the count of 
                english characters of each substring
            """

            character_dict_list = []
            for substring in substring_list:
                current_character_dict = dict()

                for char in substring:
                    if char not in current_character_dict:
                        current_character_dict[char] = 1
                    else:
                        current_character_dict[char] += 1
                character_dict_list.append(current_character_dict)
            
            return character_dict_list
        

        """
            We have to make sure that if the s1 length is more than that of s2
            we have to return false
        """

        if len(s1) > len(s2):
            return False
        main_string_char_dict = dict()
        required_substring_length = len(s1)

        for char in s1:
            if char not in main_string_char_dict:
                main_string_char_dict[char] = 1
            else:
                main_string_char_dict[char] += 1
        

        character_dict_list = compute_character_dict_list(s2, required_substring_length)

        for current_character_dict in character_dict_list:
            if current_character_dict == main_string_char_dict:
                return True
        return False

        