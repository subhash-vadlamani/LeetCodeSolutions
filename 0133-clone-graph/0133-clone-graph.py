"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
            store a hashmap where the key is the node value and the value is the node itself
        """
        root = node
        if not root:
            return root
        stack = [root]
        node_dict = {}

        while stack:
            popped_node = stack.pop()
            if popped_node.val not in node_dict:
                new_node = Node(val = popped_node.val)
                node_dict[popped_node.val] = new_node
            else:
                new_node = node_dict[popped_node.val]
            new_node_neighbors_list = []
            for neigh in popped_node.neighbors:
                if neigh.val not in node_dict:
                    # neighbor not processed before
                    # neighbor should be added to dict

                    new_neigh_node = Node(neigh.val)
                    stack.append(neigh)
                    node_dict[neigh.val] = new_neigh_node
                else:
                    new_neigh_node = node_dict[neigh.val]
                
                new_node_neighbors_list.append(new_neigh_node)
            
            new_node.neighbors = new_node_neighbors_list
        
        return node_dict[node.val]
            



        
        