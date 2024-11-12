class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        """
            Sliding Window Technique
        """

        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False
        
        s1_dict = dict()
        s2_dict = dict()

        for char in s1:
            if char not in s1_dict:
                s1_dict[char] = 1
            else:
                s1_dict[char] += 1
        

        l = 0
        r = s1_len

        for char in s2[l:r]:

            if char not in s2_dict:
                s2_dict[char] = 1
            else:
                s2_dict[char] += 1
        
        if s1_dict == s2_dict:
            return True
        while r < s2_len:
            if s2[r] not in s2_dict:
                s2_dict[s2[r]] = 1
            else:
                s2_dict[s2[r]] += 1
            
            if s2_dict[s2[l]] == 1:
                s2_dict.pop(s2[l])
            else:
                s2_dict[s2[l]] -= 1
            
            if s1_dict == s2_dict:
                return True
            r += 1
            l += 1
        
        return True if s1_dict == s2_dict else False

        