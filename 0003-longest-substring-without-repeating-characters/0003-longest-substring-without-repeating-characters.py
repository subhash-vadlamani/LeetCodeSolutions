class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            length of the longest substring without duplicate characters

            sliding window technique
        """

        i = 0
        j = 0
        char_set = set()
        """
            'j' is for adding characters
            'i' is for removing characters
        """

        max_len = 0
        curr_len = 0
        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                curr_len += 1
                j += 1
            else:
                if curr_len > max_len:
                    max_len = curr_len
                char_set.remove(s[i])
                curr_len -= 1
                i += 1
        
        if curr_len > max_len:
            max_len = curr_len
        return max_len




        