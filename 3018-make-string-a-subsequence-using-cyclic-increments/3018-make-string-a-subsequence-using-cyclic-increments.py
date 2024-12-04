class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        char_dict = {
            'a' : 0,
            'b' : 1,
            'c' : 2,
            'd' : 3,
            'e' : 4,
            'f' : 5,
            'g' : 6,
            'h' : 7,
            'i' : 8,
            'j' : 9,
            'k' : 10,
            'l' : 11,
            'm' : 12,
            'n' : 13,
            'o' : 14,
            'p' : 15,
            'q' : 16,
            'r' : 17,
            's' : 18,
            't' : 19,
            'u' : 20,
            'v' : 21,
            'w' : 22,
            'x' : 23,
            'y' : 24,
            'z' : 25,
        }
        alphabet_size = 26

        str1_len = len(str1)
        str2_len = len(str2)

        if str1_len < str2_len:
            return False
        
        j = 0
        for i in range(str1_len):
            if j == str2_len:
                break
            
            if (char_dict[str1[i]] == char_dict[str2[j]]) or ((char_dict[str1[i]] + 1) % alphabet_size == char_dict[str2[j]]):
                j += 1
        
        if j == str2_len:
            return True
        else:
            return False
        