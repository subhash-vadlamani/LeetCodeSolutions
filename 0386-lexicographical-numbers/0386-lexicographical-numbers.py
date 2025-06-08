from collections import OrderedDict
class TrieNode:
    def __init__(self):
        self.children = OrderedDict()
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    

    def insert(self, word_num: int) -> None:
        node = self.root
        word = str(word_num)
        for ch in word:
            if ch not in node.children:
                node.children[(ch)] = TrieNode()
            node = node.children[(ch)]
        node.is_end = True

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
            given an integer n, we have to sort the numbers in the range from [1, n]

            requried T.C -> O(N)
        """

        my_trie = Trie()

        for i in range(1, n + 1):
            my_trie.insert(i)
        

        answer = []
        trie_root = my_trie.root

        def dfs(trie_node, prev_key):
            # perform DFS on the trie and return the answer
            for key, child_node in trie_node.children.items():
                if child_node.is_end:
                    current_key = (prev_key + key)
                    answer.append(int(current_key))
                dfs(child_node, current_key)
            
            return
        
        dfs(trie_root, "")
        return answer



