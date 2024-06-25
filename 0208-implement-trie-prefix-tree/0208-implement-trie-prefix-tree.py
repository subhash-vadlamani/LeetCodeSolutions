class Trie:

    def __init__(self, val = None):
        self.val = val
        self.is_word = False
        self.children = dict()
        
        
        # The key of the above dict will be the substring and the value will be the Trie Node with that substring as the value
        

    def insert(self, word: str) -> None:
        
        curr = self
        
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = Trie(val = char)
                curr = curr.children[char]
        curr.is_word = True
            
            
        

    def search(self, word: str) -> bool:
        curr = self
        
        for char in word:
            
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.is_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        
        for char in prefix:
            
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True
            
            
        
        
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)