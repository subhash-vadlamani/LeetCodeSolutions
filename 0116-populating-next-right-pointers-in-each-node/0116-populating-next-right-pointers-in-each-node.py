"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        element_dict = dict()
        
        if not root:
            return root
        
        element_queue = []
        
        element_queue.append((root, 0))
        
        while element_queue:
            element_queue_member = element_queue.pop(0)
            
            if element_queue_member[1] in element_dict:
                current_level_element_list = element_dict[element_queue_member[1]]
                current_level_element_list.append(element_queue_member[0])
                
                element_dict[element_queue_member[1]] = current_level_element_list
            else:
                element_dict[element_queue_member[1]] = [element_queue_member[0]]
            
            
            element_queue_member_left_child = element_queue_member[0].left
            element_queue_member_right_child = element_queue_member[0].right
            
            element_queue_member_child_level = element_queue_member[1] + 1
            
            if element_queue_member_left_child:
                element_queue.append((element_queue_member_left_child, element_queue_member_child_level))
            
            if element_queue_member_right_child:
                element_queue.append((element_queue_member_right_child, element_queue_member_child_level))
                
        
        
        for key in element_dict:
            current_key_list = element_dict[key]
            
            for i in range(0, len(current_key_list) - 1):
                current_key_list[i].next = current_key_list[i + 1]
            
        
        return root
        