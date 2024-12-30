class Node:
    def __init__(self, character = '', eow = False):
        self.character = character
        self.eow = eow
        self.next_character_list = []

class Trie:

    def __init__(self, character = '', eow = False):
        self.root = Node(character, eow)
        

    def insert(self, word: str) -> None:
        temp = self.root

        for i in range(0, len(word)):
            new_node = None
            if i == len(word) - 1:
                for node in temp.next_character_list:
                    if node.character == word[i]:
                        node.eow = True
                        new_node = node
                        break
                
                if not new_node:
                    new_node = Node(word[i], True)
                    temp.next_character_list.append(new_node)
            
            for node in temp.next_character_list:
                if node.character == word[i]:
                    new_node = node
                    break
            if not new_node:
                new_node = Node(word[i], False)
                temp.next_character_list.append(new_node)
            temp = new_node

    def search(self, word: str) -> bool:
        temp = self.root

        for i in range(0, len(word)):
            new_node = None
            if i == len(word) - 1:
                for node in temp.next_character_list:
                    if node.character == word[i] and node.eow == True:
                        new_node = node
                        break
                if not new_node:
                    return False
                return True
                
            for node in temp.next_character_list:
                if node.character == word[i]:
                    new_node = node
                    break
            if not new_node:
                return False
            temp = new_node

            
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in range(0, len(prefix)):
            new_node = None
            for node in temp.next_character_list:
                if node.character == prefix[i]:
                    new_node = node
                    break
            if not new_node:
                return False
            temp = new_node
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)