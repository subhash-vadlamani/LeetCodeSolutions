# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final_list = []

        if not root:
            return final_list

        element_queue = []
        element_queue.append(root)

        while(element_queue):
            queue_size = len(element_queue)
            current_level_list = []

            for i in range(0, queue_size):
                current_element = element_queue.pop(0)
                current_element_value = current_element.val
                current_level_list.append(current_element_value)
                if current_element.left:
                    element_queue.append(current_element.left)
                if current_element.right:
                    element_queue.append(current_element.right)
            final_list.append(current_level_list)
        return final_list