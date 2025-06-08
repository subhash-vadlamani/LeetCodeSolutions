# from collections import OrderedDict
# class TrieNode:
#     def __init__(self):
#         self.children = OrderedDict()
#         self.is_end = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    

#     def insert(self, word_num: int) -> None:
#         node = self.root
#         word = str(word_num)
#         for ch in word:
#             if ch not in node.children:
#                 node.children[int(ch)] = TrieNode()
#             node = node.children[int(ch)]
#         node.is_end = True

# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         """
#             given an integer n, we have to sort the numbers in the range from [1, n]

#             requried T.C -> O(N)
#         """

#         my_trie = Trie()

#         for i in range(1, n + 1):
#             my_trie.insert(i)
        

#         answer = []
#         trie_root = my_trie.root

#         def dfs(trie_node):
#             # perform DFS on the trie and return the answer
#             for key, child_node in trie_node.children.items():
#                 if child_node.is_end:
#                     answer.append()




class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        # Start generating numbers from 1 to 9
        for start in range(1, 10):
            self._generate_lexical_numbers(start, n, lexicographical_numbers)
        return lexicographical_numbers

    def _generate_lexical_numbers(
        self, current_number: int, limit: int, result: List[int]
    ):
        # If the current number exceeds the limit, stop recursion
        if current_number > limit:
            return
        # Add the current number to the result
        result.append(current_number)

        # Try to append digits from 0 to 9 to the current number
        for next_digit in range(10):
            next_number = current_number * 10 + next_digit
            # If the next number is within the limit, continue recursion
            if next_number <= limit:
                self._generate_lexical_numbers(next_number, limit, result)
            else:
                break  # No need to continue if next_number exceeds limit


        