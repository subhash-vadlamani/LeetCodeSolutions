class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length = len(haystack)
        needle_length = len(needle)

        if needle_length > haystack_length:
            return -1
        
        i = 0
        while True:
            j = i + needle_length
            if j > haystack_length:
                break
            current_substring = haystack[i:j]
            if current_substring == needle:
                return i
            i += 1
        return -1
            
        