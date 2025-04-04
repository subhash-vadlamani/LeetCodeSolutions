# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # maintain a dict of nodes such that the key is the depth and the value is the list of nodes with that depth

        depth_dict = {}

        def compute_depth_dict(node, depth):
            if not node:
                return
            
            if depth in depth_dict:
                depth_dict[depth].append(node)
            else:
                depth_dict[depth] = [node]
            
            compute_depth_dict(node.left, depth + 1)
            compute_depth_dict(node.right, depth + 1)
        
        compute_depth_dict(root, 0)

        # depth_dict populated

        max_depth = sorted(depth_dict.keys())[-1] 

        deepest_nodes_list = depth_dict[max_depth]

        def compute_lca(root, node1, node2):
            if (not root) or (root.val == node1.val) or (root.val == node2.val):
                return root
            left_lca = compute_lca(root.left, node1, node2)
            right_lca = compute_lca(root.right, node1, node2)

            if left_lca and right_lca:
                return root
            elif left_lca:
                return left_lca
            else:
                return right_lca
        # print(root)
        # print(deepest_nodes_list)
        max_depth_lca = deepest_nodes_list[0]
        for i in range(1, len(deepest_nodes_list)):
            max_depth_lca = compute_lca(root, max_depth_lca, deepest_nodes_list[i])
        
        return max_depth_lca
