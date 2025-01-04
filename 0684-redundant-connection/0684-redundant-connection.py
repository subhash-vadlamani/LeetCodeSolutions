import copy
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        # Iterate in reverse and check if after removing an edge, the graph makes a tree

        def is_tree(g):
            # returns if the given adj list represents a tree

            n = len(g)
            # UNVISITED = 0
            # VISITING = 1
            # VISITED = 2
            visit_set = set()

            def dfs(i, prev):
                if i in visit_set:
                    return False
                visit_set.add(i)
                for nei in g[i]:
                    if nei != prev and not dfs(nei, i):
                        return False
                return True

            
            return dfs(1, -1) and len(visit_set) == n



        def remove_edge(my_temp, a, b):
            # removes edge between a and b
            my_temp[a].remove(b)
            my_temp[b].remove(a)

            return my_temp

        for i in range(len(edges) - 1, -1, -1):
            temp = copy.deepcopy(g)
            print(g)
            a, b = edges[i]
            temp = remove_edge(temp, a, b)

            # print(temp)

            if is_tree(temp):
                return edges[i]



        