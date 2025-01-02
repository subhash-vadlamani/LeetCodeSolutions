class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}

        # 0 means not the required kind of string
        # 1 means the required kind of string

        string_index_set = set()

        for i in range(len(words)):
            if words[i][0] in vowel_set and words[i][-1] in vowel_set:
                words[i] = 1
                string_index_set.add(i)
            else:
                words[i] = 0
        
        # convert the words list to a prefix sum list

        for i in range(1, len(words)):
            words[i] += words[i-1]
        
        answer_list = []

        for i, j in queries:
            current_answer = words[j] - words[i]
            if i in string_index_set:
                current_answer += 1
            answer_list.append(current_answer)
        
        return answer_list

        