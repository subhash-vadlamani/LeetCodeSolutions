class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        answer = 0
        word_dict = dict()

        for word in words:
            reversed_word = word[::-1]
            # print(f"word is : {word}. reversed_word is : {reversed_word}")
            if reversed_word in word_dict:
                if word_dict[reversed_word] == 1:
                    del word_dict[reversed_word]
                else:
                    word_dict[reversed_word] -= 1
                
                answer += 4
                print(f"answer is : {answer}")
            else:
                word_dict[word] = 1 + word_dict.get(word, 0)
        
        for word in word_dict:
            if word == word[::-1]:
                answer += 2
                break
        return answer


        