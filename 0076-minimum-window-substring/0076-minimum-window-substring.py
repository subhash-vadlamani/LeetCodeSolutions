class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)

        if s_len < t_len:
            return ""

        t_dict = dict()
        for i in range(t_len):
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
        s_dict = dict()

        def substring_contains_required_chars(s_dict, t_dict):
            """
                Makes sure that for every (key1, val1) pair in t_dict
                there exists (key2, val2) pair in s_dict
                such that key1 == key 2 and val2 >= val1
            """

            for _, (key, val) in enumerate(t_dict.items()):
                if key not in s_dict or val > s_dict[key]:
                    return False
            return True
        
        minimum_substring_length = float('inf')
        minimum_substring_indices = (0, 0)

        l = 0
        r = t_len - 1 
        for i in range(l, r + 1):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
        
        while r < s_len:
            if substring_contains_required_chars(s_dict, t_dict):
                current_substring_length = r - l + 1
                if current_substring_length < minimum_substring_length:
                    minimum_substring_length = current_substring_length
                    minimum_substring_indices = (l, r)
                    if current_substring_length == t_len:
                        break
                s_dict[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < s_len:
                    if s[r] not in s_dict:
                        s_dict[s[r]] = 1
                    else:
                        s_dict[s[r]] += 1
        
        if minimum_substring_length == float('inf'):
            return ""
        else:
            return s[minimum_substring_indices[0]:minimum_substring_indices[1] + 1]
        
            

        