from collections import defaultdict
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        # Adjacency list
        graph = defaultdict(list)

        for pair in similarPairs:
            first_word = pair[0]
            second_word = pair[1]

            graph[first_word].append(second_word)
            graph[second_word].append(first_word)

        def dfs(start, end, graph):
            # We need to check if there exists a 
            # path from start to end. If there exists,
            # return true, else return false

            stack = []
            visited = []
            stack.append(start)
            graph_nodes = graph.keys()

            while stack:
                current_node = stack.pop()
                if current_node == end:
                    return True
                
                visited.append(current_node)
                if tuple(visited) == tuple(graph_nodes):
                    break
                current_node_connections = graph[current_node]

                for node in current_node_connections:
                    if node not in visited:
                        stack.append(node)
                
            return False

        sentence1_length = len(sentence1)
        sentence2_length = len(sentence2)
        if sentence1_length != sentence2_length:
            return False
        for i in range(0, sentence1_length):
            sentence1_word = sentence1[i]
            sentence2_word = sentence2[i]

            if sentence1_word == sentence2_word:
                continue

            if not dfs(sentence1_word, sentence2_word, graph):
                return False
        return True







        