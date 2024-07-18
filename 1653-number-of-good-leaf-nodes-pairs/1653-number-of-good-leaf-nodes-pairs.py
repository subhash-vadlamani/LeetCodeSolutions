# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaf_nodes = []

        def dfs(node):
            if not node:
                return 
            if (not node.left) and (not node.right):
                leaf_nodes.append(node)
                return 
            

            if node.left:
                node.left.parent = node
                dfs(node.left)
            if node.right:
                node.right.parent = node
                dfs(node.right)
            
        
        root.parent = None
        dfs(root)

        good_leaf_pair_count = 0

        def dfs_leaf(node, visited, current_distance):
            nonlocal good_leaf_pair_count
            if current_distance > distance:
                return
            
            if node in leaf_nodes and node not in visited:
                visited.add(node)
                if current_distance > 0:
                    good_leaf_pair_count += 1
            
            if node.left and node.left not in visited:
                dfs_leaf(node.left, visited, current_distance + 1)
            if node.parent and node.parent not in visited:
                dfs_leaf(node.parent, visited, current_distance + 1)
            if node.right and node.right not in visited:
                dfs_leaf(node.right, visited, current_distance + 1)

            # if current_node.left and current_node.left not in current_leaf_node_list:
            #     if current_node.left in leaf_nodes:
            #         current_leaf_node_list.append(current_node.left)
            #     else:
            #         dfs_leaf(current_node.left, current_leaf_node_list, current_distance, leaf_nodes)
            
            # if current_node.parent and current_node.parent not in current_leaf_node_list:
            #     dfs_leaf(current_node.parent, current_leaf_node_list, current_distance, leaf_nodes)
            
            # if current_node.right and current_node.right not in current_leaf_node_list:
            #     if current_node.right in leaf_nodes:
            #         current_leaf_node_list.append(current_node.right)
            #     else:
            #         dfs_leaf(current_node.right, current_leaf_node_list, current_distance, leaf_nodes)

        
        
        for node in leaf_nodes:
            visited = set()
            dfs_leaf(node, visited, 0)
            # current_leaf_node_list = []
            # dfs_leaf(node, current_leaf_node_list, 0, leaf_nodes)
            # good_leaf_pair_count += len(current_leaf_node_list)

        return good_leaf_pair_count // 2