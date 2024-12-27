# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def depth(node):
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            return 1 + max(left_depth, right_depth)
        if not root:
            return True
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        
        if abs(left_depth - right_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False