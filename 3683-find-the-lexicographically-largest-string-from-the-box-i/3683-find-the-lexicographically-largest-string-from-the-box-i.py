class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        """
            How is splitting done?
        """
        if numFriends == 1:
            return word
        candidates = []
        word_len = len(word)
        for i in range(word_len):
            max_candidate_len = word_len - numFriends + 1
            candidates.append(word[i:min(i + max_candidate_len, word_len + 1)])
        
        candidates.sort(reverse=True)
        return candidates[0]
        