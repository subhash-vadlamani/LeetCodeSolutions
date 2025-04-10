from collections import defaultdict
import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        """
            Let's break down the problem:
            1 <= s1.length, s2.length <= 10 ** 4

            Let's think of brute force:
            1. calculate each and every permutation of the string s1. (TC?)
            2. Check each and every element in this list and see if it is present in s2. (TC?)

            Let's try and calculate the time complexity of step 1:

            A permutation is defined as a rearrangement of all characters in the string.

        """

        s1_char_freq_dict = defaultdict(int)

        for letter in string.ascii_lowercase:
            s1_char_freq_dict[letter] = 0

        for current_char in s1:
            s1_char_freq_dict[current_char] += 1
        
        """
            if len(s1) > len(s2), answer is false
        """

        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False
        
        """
            sliding window technique on s2 with the length of s1_len
        """

        # create the initial s2_substring_char_freq_dict

        s2_substring_char_freq_dict = defaultdict(int)

        for letter in string.ascii_lowercase:
            s2_substring_char_freq_dict[letter] = 0
            
        for i in range(0, s1_len):
            s2_substring_char_freq_dict[s2[i]] += 1
        
        l = 0
        r = s1_len - 1

        while r < s2_len - 1:
            if s1_char_freq_dict == s2_substring_char_freq_dict:
                return True
            
            print(s2_substring_char_freq_dict)
            s2_substring_char_freq_dict[s2[l]] -= 1
            l += 1
            r += 1
            s2_substring_char_freq_dict[s2[r]] += 1
        
        print(s2_substring_char_freq_dict)
        return s1_char_freq_dict == s2_substring_char_freq_dict

        