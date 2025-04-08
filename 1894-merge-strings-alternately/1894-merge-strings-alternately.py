class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)

        ans = ""

        i, j = 0, 0

        while i < word1_len or j < word2_len:

            if i < word1_len:
                ans += str(word1[i])
                i += 1
            
            if j < word2_len:
                ans += str(word2[j])
                j += 1
        
        return ans

        