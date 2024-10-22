
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        element_level_dict = dict()
        level_sums = []
        queue = [[root, 0]]

        
        def bfs(queue):
            while queue:
                popped_element = queue.pop(0)
                popped_element_node = popped_element[0]
                popped_element_level = popped_element[1]

                popped_element_node_value = popped_element_node.val
                if popped_element_level == len(level_sums):
                    level_sums.append(popped_element_node_value)
                else:
                    level_sums[popped_element_level] += popped_element_node_value
                # if popped_element_level not in element_level_dict:
                #     element_level_dict[popped_element_level] = popped_element_node_value
                # else:
                #     element_level_dict[popped_element_level] += popped_element_node_value
                
                popped_element_node_left_child = popped_element_node.left
                popped_element_node_right_child = popped_element_node.right

                if popped_element_node_left_child:
                    element_left_child = [popped_element_node_left_child, popped_element_level + 1]
                    queue.append(element_left_child)
                if popped_element_node_right_child:
                    element_right_child = [popped_element_node_right_child, popped_element_level + 1]
                    queue.append(element_right_child)
        
        bfs(queue)
        sorted_level_order_sum_list = sorted(level_sums, reverse = True)

        if k <= len(sorted_level_order_sum_list):
            return sorted_level_order_sum_list[k-1]

        else:
            return -1

        # current_min = float('inf')
        # current_rank = 0
        # for i in range(0, len(sorted_level_order_sum_list)):
        #     current_number = sorted_level_order_sum_list[i]
        #     if current_number < current_min:
        #         current_min = current_number
        #         current_rank += 1
        #     if current_rank == k:
        #         return current_min
        # return -1
        





