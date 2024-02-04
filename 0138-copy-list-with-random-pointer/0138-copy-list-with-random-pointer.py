"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current_node = head
        if not head:
            return None
        
        node_keys = []
        
        while(current_node):
            node_keys.append(current_node)
            current_node = current_node.next
        
        node_dict = {}
        
        for key in node_keys:
            node_dict[key] = {}
            node_dict[key]["val"] = key.val
            node_dict[key]["next"] = key.next
            node_dict[key]["random"] = key.random
        
         
        current_node = head
        
        node_mapping = {}
        
        while(current_node):
            new_node = Node(0)
            node_mapping[current_node] = new_node
            current_node = current_node.next
        
        
        for key in node_keys:
            new_list_node = node_mapping[key]
            new_list_node.val = node_dict[key]["val"]
            if node_dict[key]["next"]:
                new_list_node.next = node_mapping[node_dict[key]["next"]]
            else:
                new_list_node.next = None
            if node_dict[key]["random"]:
                new_list_node.random = node_mapping[node_dict[key]["random"]]
            else:
                new_list_node.random = None
        
        
        new_list_head = node_mapping[head]
        return new_list_head
            
        