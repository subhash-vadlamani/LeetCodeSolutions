class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        previous_char = None
        char_count = 0

        for c in word:
            if (previous_char and c != previous_char) or (c == previous_char and char_count == 9):
                comp += str(char_count) + str(previous_char)
                previous_char = c
                char_count = 1
            else:
                previous_char = c
                char_count += 1
        
        comp += str(char_count) + str(previous_char)
        return comp