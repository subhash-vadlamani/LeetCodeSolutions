class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        visit_set = set()

        # DFS
        def dfs(node, prev):
            
            if node in visit_set:
                return False
            visit_set.add(node)
            for nei in g[node]:
                if nei != prev and not dfs(nei, node):
                    return False
            
            return True
                    
        
        is_tree = dfs(0, -1)
        if is_tree and len(visit_set) == n:
            return True
        return False
        