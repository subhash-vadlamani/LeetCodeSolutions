class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        sentence_words = sentence.split(' ')
        for i in range(len(sentence_words)):
            if sentence_words[i].startswith(searchWord):
                return i + 1
        return -1
        