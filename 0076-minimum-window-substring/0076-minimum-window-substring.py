class Solution:
    def minWindow(self, s: str, t: str) -> str:

        m = len(s)
        n = len(t)

        """
            we need to find the minimum substring of s such that every character in t
            is included in the window.

            For this to be possible, m >=n is required.

            variable size sliding window.

            What is the best way to check if the freq dict of a substring
            contains all the elements that are present in the second string?
        """

        if m < n:
            return ""
        
        substring_dict = {}
        t_string_dict = {}

        # Populate the t_string_dict

        for i in range(n):
            if t[i] not in t_string_dict:
                t_string_dict[t[i]] = 1
            else:
                t_string_dict[t[i]] += 1
        
        def substring_contains_all_chars():

            """
                Time complexity is O(1) because the string
                contains only uppercase and lowercase english letters
            """

            for key in t_string_dict.keys():
                if key not in substring_dict or substring_dict[key] < t_string_dict[key]:
                    return False
            return True
        
        l = 0
        r = 0
        minimum_window_substring = ""
        minimum_window_size = float('inf')

        while r < m:
            substring_dict[s[r]] = 1 + substring_dict.get(s[r], 0)

            while substring_contains_all_chars():
                if r - l + 1 < minimum_window_size:
                    minimum_window_substring = s[l:r+1]
                    minimum_window_size = r - l + 1
                
                substring_dict[s[l]] -= 1
                if substring_dict[s[l]] == 0:
                    del substring_dict[s[l]]
                l += 1
            
            r += 1
            
        return minimum_window_substring


        
        



        