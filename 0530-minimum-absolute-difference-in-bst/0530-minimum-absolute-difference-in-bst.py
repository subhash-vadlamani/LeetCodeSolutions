# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if (not root) or ((not root.left) and (not root.right)):
            return float('inf') 

        left_sub_tree_answer = self.getMinimumDifference(root.left)
        right_sub_tree_answer = self.getMinimumDifference(root.right)

        if root.left and root.right:
            current_node_answer = min((root.val - self.getMaxNodeVal(root.left)), (self.getMinNodeVal(root.right) - root.val))
        elif root.left:
            current_node_answer = root.val - self.getMaxNodeVal(root.left)
        else:
            current_node_answer = self.getMinNodeVal(root.right) - root.val
        
        return min(left_sub_tree_answer, right_sub_tree_answer, current_node_answer)
    
    def getMaxNodeVal(self, root):
        if not root:
            return None
        while(root):
            current_val = root.val
            root = root.right
        
        return current_val
    
    def getMinNodeVal(self, root):
        if not root:
            return None
        
        while(root):
            current_val = root.val
            root = root.left
        return current_val

        
        