class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        answer = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[i] in words[j]:
                        answer.add(words[i])
                        break
        return list(answer)

        