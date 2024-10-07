class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        sentence1_length = len(sentence1)
        sentence2_length = len(sentence2)

        if sentence1_length != sentence2_length:
            return False
        
        similar_dict = dict()

        for similarPair in similarPairs:
            element_1 = similarPair[0]
            element_2 = similarPair[1]

            if element_1 not in similar_dict:
                similar_dict[element_1] = [element_2]
            else:
                similar_dict[element_1].append(element_2)
            
            if element_2 not in similar_dict:
                similar_dict[element_2] = [element_1]
            else:
                similar_dict[element_2].append(element_1)
        
        for i in range (0, sentence1_length):
            current_sentence1_word = sentence1[i]
            current_sentence2_word = sentence2[i]

            if (current_sentence1_word not in similar_dict or current_sentence2_word not in similar_dict[current_sentence1_word]) and (current_sentence1_word != current_sentence2_word):
                return False
        return True


        