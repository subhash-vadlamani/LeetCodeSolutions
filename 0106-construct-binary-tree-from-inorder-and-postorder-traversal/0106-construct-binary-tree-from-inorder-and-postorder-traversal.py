# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {value: idx for idx, value in enumerate(inorder)}
        
        def buildTreeHelper(left, right):
            if left > right:
                return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            index = index_map[root_val]
            
            root.right = buildTreeHelper(index + 1, right)
            root.left = buildTreeHelper(left, index - 1)
            
            return root
        return buildTreeHelper(0, len(inorder) - 1)
        