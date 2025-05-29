from collections import defaultdict
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        """
            we need to use BFS.
            We need to preprocess graph2 to find which node leads to most other nodes in 'k-1'
            steps.

            Once we do this preprocessing, we need to process every node in the graph1
            using BFS and check how many nodes can be reached in 'k' steps.
            Then, we add the preprocessed answer for graph two to it and store the 
            answers in the list

        """

        """
            Define a BFS method that takes the staring node and
            the graph
        """

        def bfs(u, k, graph):
            """
                Assume that teh implementation is done and it returns
                the number of nodes reachable from node 'u' by using atmost
                'k' steps in the given 'graph'
            """
            
            # BFS is implemented through a queue
            q = deque()
            q.append((u, -1)) # (curren_node, parent_node)
            count = 0 # Number of nodes reachable from the start node

            while q and k >= 0:

                size = len(q)
                count += size
                for _ in range(size):
                    u, parent = q.popleft()
                    for v in graph[u]:
                        if v != parent:
                            q.append((v, u))
                k -= 1

                # current_node, parent_node = q.popleft()
                # count += 1
                # for new_node in graph[current_node]:
                #     if new_node != parent_node:
                #         q.append((new_node, current_node))
                
                # k -= 1
            
            return count



        

        

        """
            Number of nodes in a tree is one more than the number of edges in the tree
        """
        n = len(edges1) + 1 
        m = len(edges2) + 1

        # Constuct the Adj list representing the trees
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for a, b in edges1:
            # Tree is an undirected graph
            graph1[a].append(b)
            graph1[b].append(a)
        
        for a, b in edges2:
            # Tree is an undirected graph
            graph2[a].append(b)
            graph2[b].append(a)
        
        # Preprocess graph2
        graph2_max = float('-inf')

        for i in range(m):
            graph2_max = max(bfs(i, k-1, graph2), graph2_max)
        
        # Now, compute the answer for the question
        answer = []
        print(graph2_max)

        for i in range(n):
            current_answer_entry = bfs(i, k, graph1) + graph2_max
            answer.append(current_answer_entry)
        
        return answer
    


        