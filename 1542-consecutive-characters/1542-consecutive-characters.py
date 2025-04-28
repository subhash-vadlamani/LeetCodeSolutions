class Solution:
    def maxPower(self, s: str) -> int:
        """
            maximum length of a non-empty substring that contains only one unique character
        """
        max_len = 1

        for i in range(len(s)):

            char_dict = dict()

            for j in range(i ,len(s)):

                char_dict[s[j]] = 1 + char_dict.get(s[j] , 0)
                char_dict_len = len(char_dict.keys())

                if char_dict_len == 1:
                    max_len = max(max_len, j - i + 1)
        
        return max_len




        