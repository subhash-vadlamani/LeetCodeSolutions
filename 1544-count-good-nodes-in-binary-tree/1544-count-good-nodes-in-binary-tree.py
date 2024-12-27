# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node_count = 0

        def is_node_good(node, current_max):
            # current_max stores the max value of the node encountered
            # till now from the root
            nonlocal good_node_count

            if node.val >= current_max:
                current_max = max(node.val, current_max)
                good_node_count += 1
            if node.left:
                is_node_good(node.left, current_max)
            if node.right:
                is_node_good(node.right, current_max)
        
        current_max = float('-inf')
        is_node_good(root, current_max)
        return good_node_count

        