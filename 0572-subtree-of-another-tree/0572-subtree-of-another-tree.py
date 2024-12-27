# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right):
            return True
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if self.is_same_tree(root, subRoot):
            return True
        
        ans = False
        if root.left:
            ans = ans or self.isSubtree(root.left, subRoot)
        if root.right:
            ans = ans or self.isSubtree(root.right, subRoot)
        return ans
        
        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or False
        