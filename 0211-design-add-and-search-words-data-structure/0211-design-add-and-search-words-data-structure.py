class WordDictionary:

    def __init__(self, val = None):
        self.val = val
        self.is_word = False
        self.children = dict()
        

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary(val = char)
            
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word:str) -> bool:
        return self._search_from_node(self, word, 0)
    
    def _search_from_node(self, node, word, index):
        if index == len(word):
            return node.is_word
        
        char = word[index]

        if char == '.':
            for child in node.children.values():
                if self._search_from_node(child, word, index+1):
                    return True
        else:
            if char in node.children:
                return self._search_from_node(node.children[char], word, index + 1)
        return False


    # def search(self, word: str) -> bool:
    #     curr = self

    #     for i in range(0, len(word)):
    #         if word[i] == '.':
    #             for key in curr.children.values():
    #                 return key.search(word[i+1:])

    #         else:
    #             if word[i] not in curr.children:
    #                 return False
    #             else:
    #                 curr = curr.children[word[i]]
    #     return curr.is_word

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)