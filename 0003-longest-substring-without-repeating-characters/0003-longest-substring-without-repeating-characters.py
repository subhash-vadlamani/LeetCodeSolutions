class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
            sliding window. 
            maintain 2 indices i, j
            maintain longest_length variable to store the length of the longest substring without duplicat
            characters

            maintain seen set
        """

        i , j = 0, 0
        longest_length = 0
        seen = set()
        s_len = len(s)

        while j < s_len:
            if s[j] not in seen:
                seen.add(s[j])
                current_length = j - i + 1
                longest_length = max(longest_length, current_length)
                j += 1
            else:
                seen.remove(s[i])
                i += 1
        return longest_length

        