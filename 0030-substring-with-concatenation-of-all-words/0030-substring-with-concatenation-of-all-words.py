import copy
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_list_length = len(words)
        word_length = len(words[0])
        concat_string_length = words_list_length * word_length
        s_len = len(s)

        if s_len < concat_string_length:
            return []
        word_dict = dict()
        for word in words:
            word_dict[word] = 1 + word_dict.get(word, 0)
        
        def check_for_words(sub_s, temp_dict, word_length):
            # we can assume that len(s) is a multiple of word_length since we check that before calling this method

            l = 0
            r = word_length
            substrings = [sub_s[i:i+word_length] for i in range(0, len(sub_s), word_length)]

            for substring in substrings:
                if substring not in temp_dict:
                    return False
                if temp_dict[substring] > 1:
                    temp_dict[substring] -= 1
                else:
                    del temp_dict[substring]
            return True
             
            

        
        # List stores the start indices of substring that is formed by concat of all the words
        answer_list = []
        l = 0
        for r in range(s_len):
            if r - l + 1 == concat_string_length:
                temp_dict = copy.deepcopy(word_dict)
                current_substring = s[l:r + 1]
                # print(current_substring)
                if check_for_words(current_substring, temp_dict, word_length):
                    answer_list.append(l)
                l += 1
        return answer_list




        