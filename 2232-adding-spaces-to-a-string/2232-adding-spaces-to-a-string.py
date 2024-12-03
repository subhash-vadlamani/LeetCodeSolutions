class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_len = len(s)
        begin = 0
        end = s_len
        final_string = ""

        for space in spaces:
            final_string += s[begin:space]
            final_string += " "

            begin = space
        
        final_string += s[begin:end]
        return final_string


        