# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        index_map = {value: idx for idx, value in enumerate(inorder)}
        
        def buildTreeHelper(left, right):
            if left > right:
                return None
            
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            
            index = index_map[root_val]
            
            root.left = buildTreeHelper(left, index - 1)
            root.right = buildTreeHelper(index + 1, right)
            
            return root
        
        return buildTreeHelper(0, len(inorder) - 1)
        