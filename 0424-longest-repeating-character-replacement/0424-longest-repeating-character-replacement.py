class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def can_create_same_letter_substring(current_string_length, char_count_dict, k):
            """
            Returns if we can create a same character substring with the given dict and k
            """
            max_key = None
            max_val = float('-inf')
            for index, (key, val) in enumerate(char_count_dict.items()):
                if val > max_val:
                    max_key = key
                    max_val = val

            if k >= current_string_length - max_val:
                return True, max_key
            return False, max_key

        char_count_dict = {}

        # Initialize pointers and max length
        l = 0
        max_length = 0

        for r in range(len(s)):
            # Update the count of the current character
            char = s[r]
            if char not in char_count_dict:
                char_count_dict[char] = 1
            else:
                char_count_dict[char] += 1

            current_string_length = r - l + 1
            can_create, current_max_key = can_create_same_letter_substring(
                current_string_length, char_count_dict, k
            )

            # If valid, update the maximum length
            if can_create:
                max_length = max(max_length, current_string_length)
            else:
                # Move the left pointer and adjust the dictionary
                left_char = s[l]
                char_count_dict[left_char] -= 1
                if char_count_dict[left_char] == 0:
                    del char_count_dict[left_char]
                l += 1

        return max_length