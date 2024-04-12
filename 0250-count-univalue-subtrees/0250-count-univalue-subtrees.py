# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        answer_list = Solution().is_tree_univalue(root)
        return answer_list[2]
    
    def is_tree_univalue(self, root):
        if not root:
            return [True, None, 0]
        if root and (not root.left) and (not root.right):
            return [True, root.val, 1]
        left_details = self.is_tree_univalue(root.left)
        right_details = self.is_tree_univalue(root.right)
        
        total_value = left_details[2] + right_details[2]
        current_tree_univalue = False
        if left_details[0] and right_details[0]:
        
            if (root.left and root.right and root.val == left_details[1] == right_details[1]) or(root.left and not root.right and root.val == left_details[1]) or (not root.left and root.right and root.val == right_details[1]):
                total_value += 1
                current_tree_univalue = True
        
        return [current_tree_univalue, root.val, total_value]
            
        
        
        
        
        