class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_dict = dict()
        t_char_dict = dict()

        for ch in s:
            s_char_dict[ch] = 1 + s_char_dict.get(ch, 0)
        
        for ch in t:
            t_char_dict[ch] = 1 + t_char_dict.get(ch, 0)
        
        return (s_char_dict == t_char_dict)
        