class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * n
        
        def dfs(i, prev, current_node_number):
            state = states[i]
            if state == VISITED:
                return current_node_number
            
            current_node_number += 1
            states[i] = VISITED

            for nei in g[i]:
                if nei != prev:
                    dfs(nei, i, current_node_number)
            return current_node_number
        
        number_of_components = 0
        for i in range(n):
            new_nodes_visited = dfs(i, -1, 0)
            # print(states)
            if new_nodes_visited:
                number_of_components += 1
        return number_of_components


        