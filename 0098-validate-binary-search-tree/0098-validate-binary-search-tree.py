# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        return (self.getTreeMax(root.left) < root.val) and (root.val < self.getTreeMin(root.right)) and (self.isValidBST(root.left) and self.isValidBST(root.right))
    
    def getTreeMin(self, root):
        if not root:
            return float('inf')
        current = root

        while(current.left):
            current = current.left
        return current.val
    
    def getTreeMax(self, root):
        if not root:
            return float('-inf')

        current = root

        while(current.right):
            current = current.right
        return current.val




# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
        
#         left_is_valid = (self.getTreeMax(root.left) < root.val) if root.left else True
#         right_is_valid = (root.val < self.getTreeMin(root.right)) if root.right else True
        
#         return left_is_valid and right_is_valid and self.isValidBST(root.left) and self.isValidBST(root.right)
    
#     def getTreeMin(self, root):
#         if not root:
#             return float('inf')
#         while root.left:
#             root = root.left
#         return root.val
    
#     def getTreeMax(self, root):
#         if not root:
#             return float('-inf')
#         while root.right:
#             root = root.right
#         return root.val
    