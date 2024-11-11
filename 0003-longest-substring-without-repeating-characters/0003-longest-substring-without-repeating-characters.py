class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_dict = dict()

        l, r = 0, 1
        len_s = len(s)
        if len_s == 0:
            return 0
        max_len = 1
        substring_dict[s[0]] = 1

        while r < len_s:
            max_len = max(max_len, r - l)
            if s[r] in substring_dict:
                substring_dict.pop(s[l])
                l += 1
            else:
                substring_dict[s[r]] = 1
                r += 1
        
        max_len = max(max_len, r - l)
        
        return max_len
            



        