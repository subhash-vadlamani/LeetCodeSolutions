from typing import Optional
class Node:
  def __init__(self, val =0, neighbors=None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []
class Solution:
  	
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
      
        cloned_nodes = {} # Dictionary to store old to new node mappings
      
        def dfs(original):
            
            if original in cloned_nodes:
                return cloned_nodes[original]
            
            
            copy  = Node(original.val)
            cloned_nodes[original] = copy
            
            #clone all neighbors
            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)