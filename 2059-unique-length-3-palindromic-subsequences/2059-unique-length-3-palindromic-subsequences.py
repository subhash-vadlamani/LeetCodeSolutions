class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_index_dict = dict()
        s_len = len(s)
        # store the first and last index for each and every character
        for i in range(s_len):
            if s[i] not in char_index_dict:
                char_index_dict[s[i]] = [i]
            elif len(char_index_dict[s[i]]) == 1:
                char_index_dict[s[i]].append(i)
            else:
                char_index_dict[s[i]][-1] = i

        def find_unique_chars_between_indices(my_list):
            i, j = my_list
            my_set = set()
            # find unique characters between (i, j) (both indices not included)

            for k in range(i + 1, j):
                my_set.add(s[k])
            return len(my_set)

        answer = 0
        for _, (key, value) in enumerate(char_index_dict.items()):
            if len(value) > 1:
                answer += find_unique_chars_between_indices(value)
        
        return answer
        
        