class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer_list = []

        for i in range(len(words)):
            word = words[i]

            if x in word:
                answer_list.append(i)
        return answer_list
        