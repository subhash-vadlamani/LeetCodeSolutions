# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        depth_dict = {}
        def depth(node):
            nonlocal depth_dict
            if not node:
                return 0
            
            if node in depth_dict:
                return depth_dict[node]
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            current_node_depth = 1 + max(left_depth, right_depth)
            depth_dict[node] = current_node_depth
            return current_node_depth
        
        def check_balanced(node):
            if not node:
                return True
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            if abs(left_depth - right_depth) > 1:
                return False
            return check_balanced(node.left) and check_balanced(node.right)
        
        depth(root)
        return check_balanced(root)
        