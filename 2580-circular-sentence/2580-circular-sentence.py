class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        string_list = sentence.split(" ")
        string_list_length = len(string_list)

        for i in range(string_list_length):
            current_string = string_list[i]
            next_string = string_list[(i + 1) % string_list_length]

            if current_string[-1] != next_string[0]:
                return False
        return True
        