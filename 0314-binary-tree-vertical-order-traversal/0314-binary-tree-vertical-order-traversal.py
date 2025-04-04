# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
            Can i do some sort of level order tranversal?
        """
        if not root:
            return []
        level_list = []

        queue = deque()
        queue.append((root, 0))
        # (node, column_number)
        while queue:
            level_elements = []
            for i in range(len(queue)):
                popped_element = queue.popleft()
                if popped_element[0].left:
                    queue.append([popped_element[0].left, popped_element[1] - 1])
                if popped_element[0].right:
                    queue.append([popped_element[0].right, popped_element[1] + 1])
                
                level_elements.append(popped_element)
            level_list.append(level_elements)
        
        column_element_dict = defaultdict(list)

        for i in range(len(level_list)):
            for j in range(len(level_list[i])):
                column_element_dict[level_list[i][j][1]].append(level_list[i][j][0].val)
        
        sorted_column_element_dict_keys = sorted(column_element_dict.keys())

        answer = []

        for key in sorted_column_element_dict_keys:
            answer.append(column_element_dict[key])
        return answer






        