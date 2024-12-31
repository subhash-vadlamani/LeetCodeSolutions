class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert_word(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True
    
    def search_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.endOfWord
    
    def search_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
            Go through the grid and construct a trie of all the words in the grid
            call the search method of trie to check if that word is present in the trie
        """

        my_trie = Trie()

        for word in words:
            my_trie.insert_word(word)
        

        m = len(board)
        n = len(board[0])

        answer_set = set()

        def dfs(i, j, node, path):
            if node.endOfWord:
                answer_set.add(path)
            
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == '#':
                return
            
            char = board[i][j]
            if char not in node.children:
                return
            
            # Explore the current character
            board[i][j] = '#'
            for x, y in [(i+1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                dfs(x, y, node.children[char], path + char)
            
            # Backtrack
            board[i][j] = char
        

        for i in range(m):
            for j in range(n):
                dfs(i, j, my_trie.root, "")
        
        return list(answer_set)

        # print(my_trie.search_prefix(""))

        # def dfs(i, j, current_word,visited):
        #     if my_trie.search_word(current_word):
        #         copy_string = current_word[:]
        #         answer_set.add(copy_string)
                
            
        #     if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited or not my_trie.search_prefix(current_word):
        #         return

        #     visited.add((i, j))
        #     current_word += str(board[i][j])
            
        #     dfs(i, j + 1, current_word, visited) # move right
        #     dfs(i, j - 1, current_word, visited) # move left
        #     dfs(i - 1, j, current_word, visited) # move up
        #     dfs(i + 1, j, current_word, visited) # move down

        #     # backtracking
        #     current_word = current_word[:-1]
        #     visited.remove((i, j))

        #     return
        
        
        
        # return list(answer_set)