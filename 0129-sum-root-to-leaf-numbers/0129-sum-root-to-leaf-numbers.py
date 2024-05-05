# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        node_stack = []
        node_stack.append((root, 0))
        root_to_leaf_sum = 0
        while node_stack:
            current_element = node_stack.pop()
            current_element_node = current_element[0]
            current_element_sum = current_element[1]
            if (not current_element_node.left) and (not current_element_node.right):
                root_to_leaf_sum += current_element_sum * 10 + current_element_node.val
            else:
                if current_element_node.right:
                    node_stack.append((current_element_node.right, current_element_sum*10 + current_element_node.val))
                if current_element_node.left:
                    node_stack.append((current_element_node.left, current_element_sum*10 + current_element_node.val))
        return root_to_leaf_sum
                
                
            
            
        