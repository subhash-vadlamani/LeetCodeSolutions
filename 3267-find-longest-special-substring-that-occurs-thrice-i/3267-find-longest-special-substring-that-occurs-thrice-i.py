class Solution:
    def maximumLength(self, s: str) -> int:
        """
            Approach 1(Brute Force): If the length of the string is l,
            the maximum possible answer would be l - 2.

            So, we start from l-2 and go to 1. if we find the answer, we return the 
            answer. if not , -1

        """
        def is_same_character_string(s):
            required_char = s[0]

            for i in range(1, len(s)):
                if s[i] != required_char:
                    return False
            return True
                
        s_len = len(s)
        for i in range(s_len - 2, 0, -1):
            j = 0
            k = i

            current_substring_dict_count = dict()
            while(k <= s_len):
                current_substring = s[j:k]
                if not is_same_character_string(current_substring):
                    j += 1
                    k += 1
                    continue
                if current_substring not in current_substring_dict_count:
                    current_substring_dict_count[current_substring] = 1
                else:
                    current_substring_dict_count[current_substring] += 1

                j += 1
                k += 1
            
            if current_substring_dict_count and max(current_substring_dict_count.values()) >= 3:
                # print(current_substring_dict_count)
                return i
        return -1
