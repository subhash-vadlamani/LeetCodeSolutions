class Node:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        def _search_for_character_(cur, i, word):
            if i == len(word):
                return cur.endOfWord

            required_character = word[i]

            if required_character != '.':
                if required_character in cur.children:
                    cur = cur.children[required_character]
                    return _search_for_character_(cur, i+1, word)
                else:
                    return False
            else:
                ans = False
                for c in cur.children:
                    ans = ans or _search_for_character_(cur.children[c], i+1, word)
                
                return ans
        cur = self.root
        return _search_for_character_(cur, 0, word)

        
                    

                


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)