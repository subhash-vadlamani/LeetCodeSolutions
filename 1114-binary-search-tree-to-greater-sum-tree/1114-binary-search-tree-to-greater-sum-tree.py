# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def inorder_traversal(root, sorted_array, sorted_array_nodes):
            if not root:
                return
            inorder_traversal(root.left, sorted_array, sorted_array_nodes)
            sorted_array.append(root.val)
            sorted_array_nodes.append(root)
            inorder_traversal(root.right, sorted_array, sorted_array_nodes)

            return
        
        global_sorted_array = []
        global_sorted_array_nodes = []

        
        

        inorder_traversal(root, global_sorted_array, global_sorted_array_nodes)

        node_sum = 0
        for i in range(0, len(global_sorted_array)):
            node_sum += global_sorted_array[i]
        
        for i in range(0, len(global_sorted_array_nodes)):
            temp = global_sorted_array_nodes[i].val
            global_sorted_array_nodes[i].val = node_sum
            node_sum -= temp

        return root



        