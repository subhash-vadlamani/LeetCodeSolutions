# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # node_level_dict = dict()

        # [level, node, parent]
        # node_level_dict[0] = [[root, None]]
        value_dict = dict()
        value_dict[root.val] = [None, 0]
        queue = [[0, root]]
        while queue:
            current_element = queue.pop(0)
            current_element_level = current_element[0]
            current_element_node = current_element[1]
            # current_element_parent = current_element[2]

            if current_element_node.left:
                # if current_element_level + 1 not in node_level_dict:
                #     node_level_dict[current_element_level + 1] = [[current_element_node.left, current_element_node]]
                # else:
                #     node_level_dict[current_element_level + 1].append([current_element_node.left, current_element_node])
                
                queue.append([current_element_level + 1, current_element_node.left])
                value_dict[current_element_node.left.val] = [current_element_node, current_element_level + 1]
            if current_element_node.right:
                # if current_element_level + 1 not in node_level_dict:
                #     node_level_dict[current_element_level + 1] = [[current_element_node.right, current_element_node]]
                # else:
                #     node_level_dict[current_element_level + 1].append([current_element_node.right, current_element_node])
                
                queue.append([current_element_level + 1, current_element_node.right])
                value_dict[current_element_node.right.val] = [current_element_node, current_element_level + 1]
        
        x_list = value_dict[x]
        y_list = value_dict[y]

        if x_list[1] == y_list[1] and x_list[0] != y_list[0]:
            return True
        else:
            return False




        