# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ascending_list = self.convertTreeToArray(root)

        return ascending_list[k-1]
    
    def convertTreeToArray(self, root):
        if not root:
            return []
        
        elif (not root.left) and (not root.right):
            return [root.val]
        else:
            left_subtree_list = self.convertTreeToArray(root.left)
            current_element_list = [root.val]
            right_subtree_list = self.convertTreeToArray(root.right)

            return left_subtree_list + current_element_list + right_subtree_list
        